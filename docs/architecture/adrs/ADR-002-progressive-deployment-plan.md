---
id: ADR-002
title: "Progressive Deployment Strategy: Local Mac mini ($0) to Lean AWS to Hardened Enterprise"
type: adr
status: accepted
created: 2026-10-10
updated: 2026-10-10
upstream:
  - "docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md"
  - "docs/project-plan/SCOPE.md"
downstream: []
tags:
  - deployment
  - devops
  - mac-mini
  - aws
  - fargate
  - cost-optimization
---

# ADR-002: Progressive Deployment Strategy: Local Mac mini to Lean AWS to Enterprise

## 0. Artifact Lineage & Traceability
- **Upstream Scope Anchor:** [`docs/project-plan/SCOPE.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/SCOPE.md) (`SCOPE-001`)
- **Upstream Architecture Record:** [`docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md) (`ADR-001`)

---

## 1. Context and Problem Statement

Building an AI teaching assistant involves compute-heavy rendering (Manim, LaTeX, FFmpeg), database storage, and low-latency API streaming. Deploying full multi-region AWS cloud infrastructure during early development introduces unnecessary baseline costs (~$150+/month) before achieving product-market fit.

The system requires a progressive 3-phase deployment model:
1. **MVP 1 ($0 Cost):** Run all services on a local Mac mini with public HTTPS tunneling for mobile testing.
2. **MVP 2 (Lean Cloud, ~$15–$25/month):** Move to simple AWS services using free tiers, public subnet Fargate tasks, and zero NAT Gateways.
3. **Commercial Production:** Transition to hardened VPCs, multi-AZ high availability, and NAT Gateways only when justified by paid user revenue.

---

## 2. Progressive Deployment Architecture

```text
┌─────────────────────────────────┐   ┌─────────────────────────────────┐   ┌─────────────────────────────────┐
│     PHASE 1: MVP 1 ($0/mo)      │   │  PHASE 2: MVP 2 (~$15-$25/mo)   │   │ PHASE 3: Commercial Enterprise  │
│        Local Mac mini           │   │         Lean AWS Cloud          │   │      Hardened Multi-AZ VPC      │
├─────────────────────────────────┤   ├─────────────────────────────────┤   ├─────────────────────────────────┤
│ • Fastify API (Local Node.js)   │   │ • Fastify API on ECS Fargate    │   │ • Fastify on ECS Fargate (HA)   │
│ • Manim Worker (Local Python)   │   │   (Public subnet, No NAT GW)    │   │ • Private subnets + NAT Gateways│
│ • Docker: Postgres 16 & Redis   │   │ • RDS Postgres db.t4g.micro     │   │ • Aurora Serverless v2 + MultiAZ│
│ • Local queue / Redis BullMQ    │   │ • Upstash Redis (Serverless $0) │   │ • AWS ElastiCache Redis Cluster │
│ • Cloudflare Tunnel (HTTPS)     │   │ • AWS SQS + S3 + CloudFront     │   │ • SQS + Fargate Spot Autoscaling│
│ • AWS Cognito (Free Tier)       │   │ • AWS Cognito (50k MAU Free)    │   │ • AWS WAF + VPC Endpoints       │
└─────────────────────────────────┘   └─────────────────────────────────┘   └─────────────────────────────────┘
```

---

## 3. Phase Specifications

### 3.1 Phase 1: MVP 1 — Local Mac mini ($0 Baseline Cost)
- **Objective:** Build and validate the core Socratic loop, mobile photo capture, and desktop canvas hand-off with zero hosting cost.
- **Compute Host:** Apple Silicon Mac mini (M-series, unified memory).
- **Service Configuration:**
  - **API Server:** Fastify running locally on Node.js 20+ (`localhost:3000`).
  - **Database & Cache:** Local Docker Compose running `postgres:16-alpine` and `redis:7-alpine`.
  - **Render Worker:** Python worker running Manim CE locally with Apple Silicon FFmpeg hardware acceleration.
  - **Queue:** Redis BullMQ or local AWS SQS emulator.
  - **Public Ingress:** **Cloudflare Tunnel (`cloudflared`)**. Provides a secure public HTTPS URL (e.g., `api-dev.yourdomain.com`) directly to the Mac mini without port forwarding or static IP fees.
  - **Auth:** AWS Cognito Free Tier (up to 50,000 MAU) or local JWT tokens for test accounts.
  - **External Dependencies:** Pay-as-you-go Gemini API (fractions of a cent per turn).

### 3.2 Phase 2: MVP 2 — Lean Cloud AWS (~$15–$25/month)
- **Objective:** Closed beta testing with real parents and students; reliable 24/7 uptime without running a local machine.
- **Service Configuration:**
  - **API Compute:** AWS ECS Fargate running a single task (0.25 vCPU, 0.5 GB RAM) in a **public subnet** with an assigned public IP. Security groups restrict ingress strictly to port 443 / Application Load Balancer.
  - **Eliminating the NAT Gateway:** Tasks run in public subnets to communicate with external LLM APIs and S3 without incurring the ~$32/month AWS NAT Gateway charge.
  - **Database:** AWS RDS PostgreSQL `db.t4g.micro` (~$15/month, or free under AWS 12-month free tier).
  - **Cache:** Upstash Serverless Redis (Free tier: 10,000 commands/day, $0 cost).
  - **Queue:** AWS SQS (1,000,000 requests/month free tier).
  - **Storage & CDN:** AWS S3 Private Bucket + CloudFront CDN (1 TB/month transfer free).
  - **Render Workers:** Fargate Spot workers triggered by SQS queue depth, rendering at 720p.
  - **Auth:** AWS Cognito (50,000 MAU free tier).

### 3.3 Phase 3: Commercial Enterprise Production (Scale & Compliance)
- **Objective:** Commercial launch, SOC2 / COPPA compliance, multi-AZ high availability.
- **Service Configuration:**
  - **Network:** Isolated Virtual Private Cloud (VPC) with Public, Private, and Database subnets across 2+ Availability Zones.
  - **Egress:** Redundant AWS NAT Gateways and VPC Endpoints for S3, SQS, and AWS Secrets Manager.
  - **Database:** Aurora Serverless v2 PostgreSQL (Multi-AZ with automatic failover).
  - **Cache:** Multi-node AWS ElastiCache Redis Cluster.
  - **Compute:** Auto-scaling ECS Fargate task fleets backed by Application Load Balancers and AWS WAF rate-limiting rules.
  - **Warm Worker Pool:** Scheduled provisioned concurrency on Fargate workers to handle peak evening homework hours (4:00 PM – 8:30 PM).

---

## 4. Phase Transition Criteria

| Transition Gate | Metrics & Trigger Conditions |
|---|---|
| **Phase 1 $\to$ Phase 2** | • Core Socratic dialogue and photo capture verified end-to-end.<br>• 15 parameterized Manim templates authored and passing golden-frame tests.<br>• Closed beta group onboarded ($\ge 10$ active parent-student pairs). |
| **Phase 2 $\to$ Phase 3** | • Sustained active users exceeding free tier limits ($> 1,000$ active students).<br>• Paying customer revenue exceeds baseline cloud costs ($> \$500/\text{month}$).<br>• Formal COPPA / institutional security audit requires private VPC isolation and WAF. |

---

## 5. Consequences

### Positive
- **Zero Financial Waste:** Enables rapid iteration during development with $0 infrastructure spend.
- **Code Parity:** Fastify, Docker PostgreSQL, Redis, and SQS/BullMQ contracts remain identical between Mac mini and AWS Fargate.
- **Clear Roadmap:** Transitions are driven by explicit user growth and revenue milestones rather than premature cloud provisioning.

### Negative / Trade-Offs
- **Mac mini Dependency in Phase 1:** Development testing requires the Mac mini to remain powered on and connected to the internet.
- **Public Subnet Care in Phase 2:** Requires strict AWS Security Group discipline (disallowing all inbound traffic except via ALB) to maintain security without a NAT Gateway.
