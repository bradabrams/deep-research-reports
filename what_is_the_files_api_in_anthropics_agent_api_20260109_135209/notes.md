# Research Notes: Anthropic Files API

## Collection Date: 2026-01-09

---

## Key Findings Summary

### What is the Files API?
The Files API is a beta feature of Anthropic's API that allows developers to upload, store, and manage files for use across multiple Claude API requests without re-uploading content each time. It was announced in October 2025 as part of a suite of four new "agent capabilities."

### Core Value Proposition
- **Upload once, use many times**: Eliminates redundant file uploads
- **Persistent storage**: Files remain available for reference across conversations
- **Workflow integration**: Designed to work with code execution tool and Agent Skills

---

## Technical Specifications

### API Endpoints
| Operation | Endpoint | Method |
|-----------|----------|--------|
| Upload | `/v1/files` | POST |
| Download | `/v1/files/{file_id}/content` | GET |
| Metadata | `/v1/files/{file_id}` | GET |
| List | `/v1/files` | GET |
| Delete | `/v1/files/{file_id}` | DELETE |

### Required Headers
```
x-api-key: $ANTHROPIC_API_KEY
anthropic-version: 2023-06-01
anthropic-beta: files-api-2025-04-14
```

### Upload Response Format
```json
{
  "id": "file_011CNha8iCJcU1wXNR6q4V8w",
  "type": "file",
  "filename": "document.pdf",
  "mime_type": "application/pdf",
  "size_bytes": 1024000,
  "created_at": "2025-01-01T00:00:00Z",
  "downloadable": false
}
```

### Referencing Files in Messages
```json
{
  "type": "document",
  "source": {
    "type": "file",
    "file_id": "file_011CNha8iCJcU1wXNR6q4V8w"
  }
}
```

---

## Limits and Constraints

| Constraint | Value |
|------------|-------|
| Max file size | 500 MB |
| Org storage limit | 100 GB |
| Filename length | 1-255 characters |
| Forbidden characters | `< > : " | ? * \ /` and unicode 0-31 |

---

## Supported File Types

### Documents
- PDF (Claude 3.5+ models)
- DOCX
- TXT
- RTF
- ODT
- HTML

### Images
- JPEG (Claude 3+ models)
- PNG
- GIF
- WebP

### For Code Execution Tool
- CSV, XLSX, JSON
- Python scripts
- Data files

---

## Pricing Model

### File Operations
**FREE**: Upload, download, list, retrieve, delete operations

### Content Usage
File content included in Messages requests is billed as **input tokens** at standard model rates.

### Code Execution Integration
- 50 free hours/org/day
- Then $0.05/hour/container

---

## Platform Availability

| Platform | Files API Support |
|----------|-------------------|
| Anthropic API Direct | ✅ Yes |
| Amazon Bedrock | ❌ No |
| Google Vertex AI | ❌ No |

---

## Integration with Agent Capabilities

### Code Execution Tool
- Upload datasets/documents → Code execution processes → Download charts/outputs
- Pre-installed libraries: pandas, matplotlib, openpyxl, python-docx, python-pptx, pillow

### Agent Skills
- Document processing skills: pptx, xlsx, docx, pdf
- Skills create files that can be downloaded via Files API
- Files not auto-saved locally

### MCP Connector
- Files API works alongside MCP for tool orchestration

---

## Asymmetric Upload/Download Rules

**IMPORTANT DESIGN DECISION:**
- Files YOU upload: Can be referenced in Messages, **cannot** be downloaded
- Files CLAUDE creates (via code execution/skills): **Can** be downloaded

This appears to be a security/anti-exfiltration measure.

---

## SDK Support

### Python SDK
```python
client.beta.files.upload(file=Path("/path/to/file"))
```

### TypeScript SDK
```typescript
const file = await client.beta.files.upload({
  file: fs.createReadStream("./document.pdf"),
  betas: ['files-api-2025-04-14']
});
```

---

## Error Handling

| Code | Meaning |
|------|---------|
| 400 | Invalid file type or filename |
| 403 | Storage limit exceeded |
| 413 | File exceeds 500 MB limit |

---

## Key Observations

1. **Beta Status Persistence**: Still in beta 8+ months after announcement (April 2025 to Jan 2026)
2. **Cloud Platform Gap**: Not available on Bedrock/Vertex - significant for enterprise customers
3. **Asymmetric Design**: Upload vs download restrictions indicate security-first design
4. **Ecosystem Integration**: Clearly designed as part of broader agent infrastructure
5. **Free Operations**: File management is free; monetization through token usage

---

## Questions for Further Research
- When will Files API exit beta?
- Roadmap for Bedrock/Vertex support?
- Retention period for inactive files?
- Rate limits on file operations?
- Future support for audio/video files?
