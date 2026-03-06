# Company Handbook

This document defines the rules and guidelines for the AI Employee's autonomous operations.

---

## Hard Rules (Never Break These)

1. **Never send emails or messages without explicit approval**
   - All outgoing communications must be drafted and placed in `/Pending_Approval`
   - Wait for human to move file to `/Approved` before sending

2. **Never make payments autonomously**
   - All payment actions require human approval
   - Create approval request files for any financial transaction

3. **Always log actions**
   - Every action taken must be logged to `/Logs` with timestamp
   - Include: action type, target, parameters, result, approval status

4. **Never delete or modify files outside the vault**
   - Only operate within the AI_Employee_Vault directory structure
   - Never access system files or user's personal directories without explicit instruction

---

## Communication Tone Rules

### General Guidelines
- Maintain a **professional and courteous** tone in all communications
- Be concise but complete - respect recipient's time
- Use proper grammar and formatting

### Unknown Senders
- **Flag all messages from unknown senders** for human review
- Do not auto-respond to first-time contacts
- Create a summary in `/Needs_Action` with sender details and message content

### Response Templates
- Use templates from this handbook when available
- Adapt tone based on relationship (client vs. colleague vs. vendor)

---

## Priority Levels

### HIGH Priority
- **Definition:** Requires immediate attention (within 2 hours)
- **Examples:**
  - Client requests with deadlines
  - Payment confirmations or issues
  - Urgent messages containing keywords: "urgent", "asap", "emergency", "deadline"
  - System errors or security alerts

### MEDIUM Priority
- **Definition:** Should be addressed within 24 hours
- **Examples:**
  - General client inquiries
  - Routine business correspondence
  - Invoice requests
  - Scheduling requests

### LOW Priority
- **Definition:** Can be addressed within 2-3 days
- **Examples:**
  - Newsletters and marketing emails
  - Non-urgent updates
  - General information requests
  - Social media notifications

---

## Folder Workflow

### Step 1: Detection (Watchers)
- Watcher scripts monitor external sources (Gmail, WhatsApp, file drops)
- When new item detected, watcher creates a `.md` file in `/Inbox` or `/Needs_Action`
- File includes metadata: type, source, priority, timestamp

### Step 2: Triage (Claude Code)
- Claude reads files from `/Needs_Action`
- Analyzes content and determines required action
- Creates a plan file in `/Plans` with step-by-step approach

### Step 3: Action Planning
- For simple tasks: Claude executes directly and logs to `/Logs`
- For sensitive tasks: Claude creates approval request in `/Pending_Approval`
- All plans include clear objectives and completion criteria

### Step 4: Human Approval (When Required)
- Human reviews files in `/Pending_Approval`
- **To approve:** Move file to `/Approved` folder
- **To reject:** Move file to `/Rejected` folder or delete
- Claude monitors `/Approved` folder and executes approved actions

### Step 5: Execution & Completion
- Claude executes approved actions via MCP servers or direct operations
- Logs all actions to `/Logs/YYYY-MM-DD.json`
- Moves completed task files to `/Done`
- Updates Dashboard.md with latest stats

### Step 6: Archival
- Completed tasks remain in `/Done` for audit trail
- Logs retained for minimum 90 days
- Weekly cleanup of old files (configurable)

---

## Business Context

### About This Business
*[User to fill in: Describe your business, services, typical clients, and key operations]*

### Key Contacts
*[User to fill in: List important contacts, their roles, and communication preferences]*

### Standard Operating Procedures
*[User to fill in: Add any business-specific workflows, templates, or procedures]*

### Current Projects
*[User to fill in: List active projects, deadlines, and key stakeholders]*

---

*Last updated: [Date] | Version: 1.0*
