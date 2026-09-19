# GitHub Actions secrets

CI for SysEx needs **zero** repository secrets. The workflow only checks out public code and runs unittest.
This connector cannot write secret values. Do not paste keys into git or into chat.

Operator path if a later CD job ever exists (still hold=true now):
Settings → Secrets and variables → Actions → New repository secret.

Name allowlist only (empty until execute is explicitly opened):
- none required

Forbidden in git: XAI_API_KEY, tokens, ZeroTier network id, Cloudflare origin credentials, Coinbase keys.
GARAS class CREDENTIAL: mention of a secret in an intent is deny, not a reason to commit it.
GITHUB_TOKEN is injected by Actions itself. Do not store a PAT in the repo to replace it.
