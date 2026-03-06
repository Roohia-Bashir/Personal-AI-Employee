# 🤖 Personal AI Employee

> **Your life and business on autopilot.** Local-first, agent-driven, human-in-the-loop autonomous assistant built with Claude Code.

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Claude Code](https://img.shields.io/badge/Claude-Code-purple.svg)](https://claude.com/product/claude-code)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Hackathon 0](https://img.shields.io/badge/Hackathon-0-green.svg)](hackathon.md)

---

## 📋 Table of Contents

- [What is This?](#-what-is-this)
- [Architecture Overview](#-architecture-overview)
- [Tier System](#-tier-system)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Skills & Capabilities](#-skills--capabilities)
- [Security & Privacy](#-security--privacy)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

---

## 🎯 What is This?

The **Personal AI Employee** is an autonomous AI agent that manages your personal and business affairs 24/7. Think of it as hiring a senior employee who:

- 📧 **Triages your Gmail** and drafts replies
- 💬 **Monitors WhatsApp** for urgent client messages
- 📱 **Posts on LinkedIn, Twitter, Facebook** to generate business leads
- 💰 **Manages accounting** via Odoo ERP integration
- 📊 **Generates weekly CEO briefings** with revenue analysis and bottleneck detection
- ✅ **Requires human approval** for sensitive actions (payments, unknown contacts)

### Why Build This?

**Digital FTE (Full-Time Equivalent) Economics:**

| Metric | Human FTE | Digital FTE |
|--------|-----------|-------------|
| **Availability** | 40 hrs/week | 168 hrs/week (24/7) |
| **Monthly Cost** | $4,000-$8,000 | $500-$2,000 |
| **Ramp-up Time** | 3-6 months | Instant |
| **Cost per Task** | ~$5.00 | ~$0.50 |
| **Annual Hours** | ~2,000 | ~8,760 |

**Result:** 85-90% cost reduction with 4x availability.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXTERNAL SOURCES                             │
│     Gmail    │    WhatsApp    │    Bank APIs    │    Files     │
└────────┬─────────────┬─────────────┬──────────────┬─────────────┘
         │             │             │              │
         ▼             ▼             ▼              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PERCEPTION LAYER (Watchers)                   │
│   GmailWatcher │ WhatsAppWatcher │ LinkedInPoster │ etc.       │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              OBSIDIAN VAULT (Local Knowledge Base)              │
│  /Needs_Action  │  /Plans  │  /Pending_Approval  │  /Done      │
│  Dashboard.md   │  Company_Handbook.md  │  Business_Goals.md   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   REASONING LAYER (Claude Code)                 │
│         Read → Think → Plan → Request Approval → Act            │
└────────────────────────────┬────────────────────────────────────┘
                             │
              ┌──────────────┴───────────────┐
              ▼                              ▼
┌──────────────────────────┐    ┌───────────────────────────────┐
│  HUMAN-IN-THE-LOOP       │    │     ACTION LAYER (MCP)        │
│  Review & Approve        │───▶│  Email │ WhatsApp │ Social   │
└──────────────────────────┘    │  Odoo  │ Calendar │ Browser  │
                                └───────────────────────────────┘
```

### Core Components

1. **Watchers** (Python) - Monitor external sources and create action files
2. **Vault** (Obsidian) - Local markdown-based knowledge base and dashboard
3. **Claude Code** - AI reasoning engine that processes tasks autonomously
4. **MCP Servers** - Model Context Protocol servers for external actions
5. **Skills** - 15 specialized Claude Code skills for different workflows
6. **Orchestrator** - Master process managing all components

---

## 🎖️ Tier System

This project implements a **Gold Tier** autonomous AI employee. Here's the progression:

### 🥉 Bronze Tier (Foundation)
**Time:** 8-12 hours | **Status:** ✅ Complete

- ✅ Obsidian vault with Dashboard.md and Company_Handbook.md
- ✅ One working watcher (Gmail OR filesystem)
- ✅ Claude Code reading/writing to vault
- ✅ Basic folder structure: /Inbox, /Needs_Action, /Done
- ✅ All functionality as Agent Skills

### 🥈 Silver Tier (Functional Assistant)
**Time:** 20-30 hours | **Status:** ✅ Complete

- ✅ Two or more watchers (Gmail + WhatsApp + LinkedIn)
- ✅ Automatic LinkedIn posting for business lead generation
- ✅ Claude reasoning loop creating Plan.md files
- ✅ One working MCP server (email sending)
- ✅ Human-in-the-loop approval workflow
- ✅ Basic scheduling via orchestrator
- ✅ All functionality as Agent Skills

### 🥇 Gold Tier (Autonomous Employee)
**Time:** 40+ hours | **Status:** ✅ Complete

- ✅ Full cross-domain integration (Personal + Business)
- ✅ Odoo Community accounting system integration via MCP
- ✅ Facebook and Instagram integration with posting
- ✅ Twitter (X) integration with posting
- ✅ Multiple MCP servers (7 total: Email, WhatsApp, LinkedIn, Twitter, Facebook, Calendar, Odoo)
- ✅ Weekly Business and Accounting Audit with CEO Briefing
- ✅ Error recovery and graceful degradation
- ✅ Comprehensive audit logging
- ✅ Ralph Wiggum loop for autonomous multi-step tasks
- ✅ Complete documentation
- ✅ All functionality as Agent Skills (15 skills)

### 💎 Platinum Tier (Production-Ready)
**Time:** 60+ hours | **Status:** 🚧 Roadmap

- ⏳ 24/7 cloud deployment (Oracle/AWS free tier)
- ⏳ Work-zone specialization (Cloud drafts, Local approves)
- ⏳ Vault sync via Git/Syncthing
- ⏳ Cloud Odoo deployment with HTTPS
- ⏳ Agent-to-agent communication
- ⏳ Health monitoring and auto-recovery

---

## 🚀 Quick Start

### Prerequisites

| Component | Version | Purpose |
|-----------|---------|---------|
| [Python](https://python.org) | 3.13+ | Watchers & orchestration |
| [Claude Code](https://claude.com/product/claude-code) | Latest | AI reasoning engine |
| [Obsidian](https://obsidian.md) | 1.10.6+ | Knowledge base GUI |
| [Node.js](https://nodejs.org) | 24+ LTS | MCP servers |
| [uv](https://docs.astral.sh/uv/) | Latest | Python package manager |

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/Personal-AI-Employee.git
cd Personal-AI-Employee

# 2. Install Python dependencies
uv sync

# 3. Copy environment template
cp .env.example .env

# 4. Configure your credentials (see Configuration section)
nano .env

# 5. Set up Gmail API credentials
# Download credentials.json from Google Cloud Console
# Place in project root

# 6. Run initial setup (dry-run mode)
uv run python main.py --dry-run

# 7. Open vault in Obsidian
# File → Open Vault → Select AI_Employee_Vault/
```

### First Run

```bash
# Test individual watchers
uv run python main.py --gmail --dry-run      # Test Gmail watcher
uv run python main.py --whatsapp --dry-run   # Test WhatsApp watcher
uv run python main.py --linkedin --dry-run   # Test LinkedIn poster

# Run full orchestrator (all watchers)
uv run python main.py --dry-run

# Production mode (disable dry-run in .env first!)
uv run python main.py
```

---

## 📁 Project Structure

```
Personal-AI-Employee/
├── AI_Employee_Vault/          # Obsidian vault (your AI's brain)
│   ├── Needs_Action/           # New tasks detected by watchers
│   ├── Plans/                  # Task execution plans
│   │   ├── linkedin_queue/     # Queued LinkedIn posts
│   │   ├── twitter_queue/      # Queued Twitter posts
│   │   └── facebook_queue/     # Queued Facebook posts
│   ├── Pending_Approval/       # Actions awaiting human approval
│   ├── Approved/               # Human-approved actions
│   ├── Rejected/               # Rejected actions
│   ├── Done/                   # Completed tasks (audit trail)
│   ├── Logs/                   # Action logs (JSON)
│   ├── Briefings/              # Weekly CEO briefings
│   ├── Dashboard.md            # Real-time status dashboard
│   ├── Company_Handbook.md     # AI behavior rules
│   └── Business_Goals.md       # Business objectives & KPIs
│
├── watchers/                   # Perception layer (Python)
│   ├── base_watcher.py         # Abstract watcher template
│   ├── gmail_watcher.py        # Gmail monitoring
│   ├── whatsapp_watcher.py     # WhatsApp monitoring
│   ├── linkedin_poster.py      # LinkedIn auto-posting
│   ├── twitter_poster.py       # Twitter auto-posting
│   ├── facebook_poster.py      # Facebook auto-posting
│   ├── filesystem_watcher.py   # File drop monitoring
│   ├── hitl_approval_watcher.py # Human approval processor
│   ├── plan_creator.py         # Auto-plan generation
│   └── config.py               # Configuration loader
│
├── mcp_servers/                # Action layer (MCP)
│   ├── email_mcp.py            # Gmail sending
│   ├── whatsapp_mcp.py         # WhatsApp sending
│   ├── linkedin_mcp.py         # LinkedIn posting
│   ├── twitter_mcp.py          # Twitter posting
│   ├── facebook_mcp.py         # Facebook posting
│   ├── calendar_mcp.py         # Google Calendar
│   └── odoo_mcp.py             # Odoo ERP integration
│
├── .claude/skills/             # Claude Code skills (15 total)
│   ├── plan-creator/           # Meta-orchestration skill
│   ├── gmail-triage/           # Email processing
│   ├── gmail-sender/           # Email sending
│   ├── whatsapp-triage/        # WhatsApp processing
│   ├── whatsapp-sender/        # WhatsApp sending
│   ├── hitl-approval/          # Human-in-the-loop safety
│   ├── linkedin-poster/        # LinkedIn content generation
│   ├── twitter-poster/         # Twitter content generation
│   ├── facebook-poster/        # Facebook content generation
│   ├── daily-briefing/         # Weekly CEO briefing
│   ├── subscription-audit/     # Recurring payment analysis
│   ├── odoo-accounting/        # Invoice & customer management
│   ├── calendar-scheduler/     # Meeting scheduling
│   └── browsing-with-playwright/ # Web automation
│
├── main.py                     # Entry point
├── orchestrator.py             # Master process
├── process_watchdog.py         # Health monitoring
├── cron_setup.sh               # Scheduled task installer
├── .env.example                # Environment template
├── CLAUDE.md                   # Claude Code configuration
├── hackathon.md                # Full hackathon specification
└── README.md                   # This file
```

---

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# ── Core Paths ────────────────────────────────────────────────
VAULT_PATH=./AI_Employee_Vault
DROP_FOLDER_PATH=./drop_folder

# ── Gmail ─────────────────────────────────────────────────────
GMAIL_CREDENTIALS_PATH=./credentials.json
GMAIL_TOKEN_PATH=./watchers/token.pickle
CHECK_INTERVAL=120  # seconds

# ── WhatsApp ──────────────────────────────────────────────────
WHATSAPP_SESSION_PATH=./.whatsapp_session
WHATSAPP_CHECK_INTERVAL=30

# ── LinkedIn ──────────────────────────────────────────────────
LINKEDIN_SESSION_PATH=./.linkedin_session
LINKEDIN_CHECK_INTERVAL=3600  # 1 hour

# ── Twitter ───────────────────────────────────────────────────
TWITTER_SESSION_PATH=./.twitter_session
TWITTER_CHECK_INTERVAL=300  # 5 minutes

# ── Facebook ──────────────────────────────────────────────────
FACEBOOK_SESSION_PATH=./.facebook_session
FACEBOOK_CHECK_INTERVAL=300

# ── Behavior ──────────────────────────────────────────────────
DRY_RUN=true  # Set to 'false' for production mode
```

### Gmail API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project
3. Enable Gmail API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download `credentials.json` to project root
6. Run `uv run python main.py --gmail --dry-run` to authenticate

### WhatsApp Session Setup

```bash
# Run WhatsApp watcher once to authenticate
uv run python main.py --whatsapp --dry-run

# Scan QR code when browser opens
# Session saved to .whatsapp_session/
```

### Social Media Sessions

```bash
# LinkedIn: Authenticate via browser
uv run python main.py --linkedin --dry-run

# Twitter: Export cookies using browser extension
# Place cookies.json in .twitter_session/

# Facebook: Export cookies using browser extension
# Place cookies.json in .facebook_session/
```

---

## 💻 Usage

### Running the AI Employee

```bash
# Full orchestrator (all watchers + scheduling)
uv run python main.py

# Individual watchers (for testing)
uv run python main.py --gmail
uv run python main.py --whatsapp
uv run python main.py --linkedin
uv run python main.py --twitter
uv run python main.py --facebook
uv run python main.py --hitl

# Trigger weekly CEO briefing manually
uv run python main.py --briefing

# Safe mode (no external actions)
uv run python main.py --dry-run
```

### Scheduled Tasks (Cron)

```bash
# Install cron jobs (Mac/Linux)
./cron_setup.sh install

# Scheduled tasks:
# - Daily briefing: Monday 8:00 AM
# - Subscription audit: Sunday 8:00 PM
```

### Workflow Example: Email Triage

1. **Detection:** Gmail watcher detects important email
2. **Action File:** Creates `EMAIL_20260306_143000_subject.md` in `/Needs_Action/`
3. **Reasoning:** Claude Code reads email, detects intent, assigns priority
4. **Planning:** Creates `PLAN_EMAIL_20260306_143000.md` in `/Plans/`
5. **Approval:** Writes draft reply to `/Pending_Approval/`
6. **Human Review:** You move file to `/Approved/` or `/Rejected/`
7. **Execution:** Email MCP sends approved reply
8. **Logging:** Action logged to `/Logs/2026-03-06.json`
9. **Archival:** All files moved to `/Done/`

---

## 🎓 Skills & Capabilities

The AI Employee has **15 specialized skills** implemented as Claude Code Agent Skills:

### Meta-Orchestration
- **plan-creator** - Analyzes tasks and creates structured execution plans

### Communication
- **gmail-triage** - Detects email intent, assigns priority, routes to approval
- **gmail-sender** - Sends approved emails via Gmail MCP
- **whatsapp-triage** - Processes WhatsApp messages, drafts replies
- **whatsapp-sender** - Sends approved WhatsApp messages

### Content Generation
- **linkedin-poster** - Generates professional LinkedIn posts (1,300 char limit)
- **twitter-poster** - Generates punchy tweets (250 char limit)
- **facebook-poster** - Generates community-engaging Facebook posts (40-80 words)

### Business Intelligence
- **daily-briefing** - Generates weekly CEO briefing with revenue analysis
- **subscription-audit** - Detects wasteful recurring payments
- **odoo-accounting** - Manages customers and invoices in Odoo ERP

### Utilities
- **calendar-scheduler** - Schedules meetings, checks availability
- **hitl-approval** - Human-in-the-loop safety mechanism
- **browsing-with-playwright** - Web automation for complex tasks

### Skill Invocation

Skills are automatically invoked by Claude Code based on task context. You can also manually trigger them:

```bash
# In Claude Code CLI
/plan-creator "Create invoice for Client A"
/gmail-triage "Process urgent emails"
/daily-briefing "Generate this week's briefing"
```

---

## 🔒 Security & Privacy

### Core Principles

1. **Local-First:** All data stored locally in Obsidian vault
2. **Human-in-the-Loop:** Sensitive actions require explicit approval
3. **Audit Trail:** Every action logged to `/Logs/` with timestamp
4. **DRY_RUN Mode:** Test safely without real external actions

### Credential Management

```bash
# ✅ DO: Use environment variables
export GMAIL_API_KEY="your-key"

# ✅ DO: Use .env file (already in .gitignore)
echo "GMAIL_API_KEY=your-key" >> .env

# ❌ DON'T: Hardcode credentials in code
# ❌ DON'T: Commit .env to git
# ❌ DON'T: Store credentials in vault
```

### Permission Boundaries

| Action Category | Auto-Approve | Always Require Approval |
|----------------|--------------|-------------------------|
| **Email replies** | Known contacts | New contacts, bulk sends |
| **Payments** | < $50 recurring | All new payees, > $100 |
| **Social media** | Scheduled posts | Replies, DMs |
| **File operations** | Create, read | Delete, move outside vault |

### What Gets Logged

Every action creates a JSON log entry:

```json
{
  "timestamp": "2026-03-06T14:30:00Z",
  "action_type": "email_sent",
  "actor": "claude_code",
  "target": "client@example.com",
  "parameters": {"subject": "Invoice #123"},
  "approval_status": "approved",
  "approved_by": "human",
  "result": "success"
}
```

Logs retained for minimum 90 days in `/Vault/Logs/`.

---

## 🐛 Troubleshooting

### Common Issues

#### Gmail API 403 Forbidden
```bash
# Solution: Enable Gmail API in Google Cloud Console
# Verify OAuth consent screen is configured
```

#### WhatsApp Session Expired
```bash
# Solution: Re-authenticate
uv run python main.py --whatsapp --dry-run
# Scan QR code when browser opens
```

#### Watcher Stops Running
```bash
# Solution: Use process manager (PM2)
npm install -g pm2
pm2 start main.py --interpreter python3
pm2 save
pm2 startup
```

#### Claude Code Not Reading Vault
```bash
# Solution: Verify working directory
cd /path/to/Personal-AI-Employee
uv run python main.py

# Or use --cwd flag
claude --cwd /path/to/AI_Employee_Vault
```

#### MCP Server Won't Connect
```bash
# Solution: Check server process is running
ps aux | grep mcp

# Verify path in ~/.claude/settings.json
# Ensure absolute paths, not relative
```

### Debug Mode

```bash
# Enable verbose logging
export LOG_LEVEL=DEBUG
uv run python main.py

# Check logs
tail -f logs/orchestrator.log
tail -f AI_Employee_Vault/Logs/$(date +%Y-%m-%d).json
```

### Health Check

```bash
# Run process watchdog
uv run python process_watchdog.py

# Check all watchers are alive
ps aux | grep -E "(gmail|whatsapp|linkedin)_watcher"
```

---

## 📊 Monitoring & Observability

### Dashboard.md

Real-time status dashboard in Obsidian:

```markdown
# AI Employee Dashboard

**Last Updated:** 2026-03-06 14:30:00

## Status
- 🟢 All systems operational
- 📧 Gmail: 3 pending actions
- 💬 WhatsApp: 1 urgent message
- 📱 Social: 2 posts queued

## This Week
- Emails processed: 47
- Invoices sent: 3
- Social posts: 12
- Time saved: 8.5 hours

## Pending Approvals
- APPROVAL_invoice_client_a_20260306.md
- APPROVAL_email_unknown_20260306.md
```

### Weekly CEO Briefing

Generated every Monday at 8:00 AM:

```markdown
# Monday Morning CEO Briefing

## Executive Summary
Strong week with revenue ahead of target. One bottleneck identified.

## Revenue & Financial Health
- **This Week:** $2,450
- **MTD:** $4,500 (45% of $10,000 target)
- **Trend:** On track

## Completed Tasks
- [x] Client A invoice sent and paid
- [x] Project Alpha milestone 2 delivered
- [x] Weekly social media posts scheduled

## Bottlenecks
| Task | Expected | Actual | Delay |
|------|----------|--------|-------|
| Client B proposal | 2 days | 5 days | +3 days |

## Proactive Suggestions
- **Notion:** No activity in 45 days. Cost: $15/month.
  - [ACTION] Cancel subscription?
```

---

## 🤝 Contributing

Contributions welcome! This is a hackathon project that can evolve into a production-ready system.

### Development Setup

```bash
# Fork and clone
git clone https://github.com/yourusername/Personal-AI-Employee.git
cd Personal-AI-Employee

# Create feature branch
git checkout -b feature/your-feature

# Install dev dependencies
uv sync --dev

# Run tests
pytest tests/

# Submit PR
```

### Roadmap to Platinum Tier

- [ ] Cloud deployment (Oracle/AWS free tier)
- [ ] Work-zone specialization (Cloud/Local split)
- [ ] Vault sync via Git automation
- [ ] Agent-to-agent communication protocol
- [ ] Health monitoring dashboard
- [ ] Mobile app for approvals
- [ ] Voice interface integration
- [ ] Multi-user support

---

## 📚 Resources

### Learning Materials

- [Claude Code Documentation](https://agentfactory.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows)
- [Agent Skills Guide](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [MCP Introduction](https://modelcontextprotocol.io/introduction)
- [Hackathon Specification](hackathon.md)

### Video Tutorials

- [Claude Code + Obsidian Integration](https://www.youtube.com/watch?v=sCIS05Qt79Y)
- [Building AI Agent Teams](https://www.youtube.com/watch?v=0J2_YGuNrDo)
- [Claude Agent Skills](https://www.youtube.com/watch?v=nbqqnl3JdR0)

### Community

- [Hackathon Submission Form](https://forms.gle/JR9T1SJq5rmQyGkGA)
- [Discord Community](#) (Coming soon)
- [Weekly Research Meetings](#) (Wednesdays)

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

Built for **Hackathon 0: Building Autonomous FTEs in 2026**

- **Claude Code** by Anthropic - AI reasoning engine
- **Obsidian** - Local-first knowledge base
- **Model Context Protocol (MCP)** - Standardized tool integration
- **Playwright** - Browser automation
- **Odoo Community** - Open-source ERP

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/Personal-AI-Employee/issues)
- **Documentation:** [Full Hackathon Spec](hackathon.md)
- **Email:** roohiabashir1994@gmail.com

---

<div align="center">

**Built with ❤️ using Claude Code**

*Transform your business with autonomous AI employees*

[Get Started](#-quick-start) • [View Demo](#) • [Read Docs](hackathon.md)

</div>
