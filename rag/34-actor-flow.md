# Actor flowchart

Label ≠ path. Write vs bundle is decided by whether that session has a GitHub connector.

```mermaid
flowchart TD
  OP[Operator] --> Q{theme}
  Q --> S[GRK / GPT / GEM / CLA]
  S --> C{GitHub connector in this session}
  C -->|yes| GIT[commit main]
  C -->|no| B[bundle paths + files]
  B --> W{who can push}
  W -->|session with connector or Operator| GIT
  W -->|conflict execute hold secrets| NIK[NIKITA escalate]
  NIK --> GIT
  GIT --> OP
```

GEM: no connector observed. CLA: no connector in the last bundle. This Grok chat session: connector present.
NIKITA only on escalate.
