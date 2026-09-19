// Sketch only. Not built by scripts/ci.sh.
// cargo add serde serde_json --features serde/derive

use serde::Deserialize;
use serde_json::Value;

#[derive(Debug, Deserialize)]
pub struct Packet {
    pub schema: String,
    pub from: String,
    pub to: String,
    pub verb: String,
    pub text: String,
    pub execute: bool,
    pub live_write: bool,
    pub a4b: Value,
    pub amb: Value,
    pub bilo: Value,
    pub garas: Value,
    pub atm: Value,
    pub rc: Value,
    pub trace_verify: Option<Value>,
}

pub fn parse(raw: &str) -> Result<Packet, serde_json::Error> {
    let packet: Packet = serde_json::from_str(raw)?;
    if packet.execute || packet.live_write {
        // caller must still treat as hold; this crate does not flip rails
    }
    Ok(packet)
}
