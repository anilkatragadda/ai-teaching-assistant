# Desktop applications and web wrappers

Apply to macOS, Windows, Linux, and desktop wrappers such as Electron/Tauri.
A wrapper needs this reference and [Web](web.md); browser content alone does not
prove a desktop app's native behavior.

## Respect the operating system

Use platform conventions for menus, shortcuts, window chrome, dialogs, file
pickers, selection, and contextual actions. Detect the actual toolkit and
target OSes: AppKit/SwiftUI, WinUI/WPF, GTK/Qt, JavaFX, Avalonia, Flutter, or the
existing web wrapper. Do not rewrite toolkit choice.

| Concern | Design requirement |
| --- | --- |
| Keyboard | Complete primary tasks without a pointer; visible focus and logical traversal |
| Shortcuts | Platform-appropriate modifiers, discoverable menu labels, no text-editing conflicts |
| Menus | Use the established app/menu model; context menus supplement visible access |
| Selection | Predictable single/multi/range selection and bulk-action scope |
| File work | Native picker/save behavior where available; clear progress and failure recovery |
| Windowing | Useful resize/minimum size, restored state, and no inaccessible offscreen windows |
| Unsaved work | Clear saved/modified status, appropriate undo and close/quit protection |

Do not replace working system title bars with decorative draggable rectangles.
If a custom title bar already exists, preserve drag regions, interactive
exclusions, maximize/snap/fullscreen behavior, and accessible window controls.

## Composition and density

Use available space for task context, comparison, or master/detail panes rather
than larger cards. Keep dense controls legible and navigable; density is not
permission to shrink text indiscriminately or remove labels.

Resizable panes need clear handles, limits, usable keyboard alternatives, and
stable focus. Toolbars should prioritize actions and provide discoverable
overflow. Preserve the task at compact window sizes rather than assuming a
maximized monitor.

Test maximized and narrow windows, display scaling, mixed-DPI monitors where
supported, and window state restoration. Units and text scaling follow the
toolkit; a phone's 44 pt touch default is not a universal desktop minimum.
Touch-enabled desktop layouts still need suitable touch affordances.

## Accessibility and system integration

Use platform accessibility semantics, roles, states, and focus APIs. Verify
VoiceOver on macOS, Narrator on Windows, or available Linux assistive tooling
for shipped targets. Support increased contrast, Windows forced/high-contrast
colors, reduced motion, and display/text scaling as applicable.

Keep clipboard, text selection, native scrolling, drag/drop, and keyboard
editing familiar. Provide a non-drag path. Do not block common OS shortcuts or
make keyboard shortcuts the only way to discover an action.

## Wrappers and trust boundaries

Test behavior in the packaged app, including native dialogs/menus, app protocol
links, multi-window focus, offline status, and OS chrome. Browser tests remain
valuable for renderer content but are not a substitute for app-level checks.

Use the existing approved bridge for file/clipboard/OS capabilities; never
enable broad renderer privileges or arbitrary native execution to simplify UI.
Show clear errors for denied access or unavailable capabilities.
Do not expose sensitive filesystem paths unnecessarily in user-facing messages.

## Performance and verification

Keep long operations off the UI thread, with honest progress and cancellation
where supported. Check large datasets/files, rendering cost, startup, memory,
and window resizing with the actual toolkit's tools.

Validate a primary keyboard-only flow, menu/contextual access, undo/cancel,
file-dialog behavior when relevant, and unsaved close/quit. Capture the real
app at representative window sizes and scale factors. Report unavailable OS
validation explicitly; testing one wrapper renderer does not prove all OSes.
