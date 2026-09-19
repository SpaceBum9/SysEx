// Sketch. Not built by CI. live_rail=false so this does not bind.

// Tokio would normally: Runtime -> TcpListener::bind -> accept loop.
// SysEx ATM host is not ready. Do not bind moreatm or 0.0.0.0 here.

pub fn hold_reason() -> &'static str {
    "live_rail=false; no tokio listener"
}
