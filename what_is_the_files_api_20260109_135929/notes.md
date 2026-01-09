# Research Notes: Files API

## Collection 1 - January 9, 2026

### Key Findings Summary

#### 1. AI Provider Files APIs - Core Comparison

| Feature | OpenAI | Anthropic | Google Gemini |
|---------|--------|-----------|---------------|
| Max File Size | 512 MB (8 GB with Uploads API) | 500 MB | 2 GB (up to 5 GB recently) |
| Total Storage | 1 TB/org | 100 GB/org | 20-50 GB/project |
| Retention | Permanent (except batch: 30 days) | Permanent | 48 hours auto-delete |
| Beta Status | GA | Beta (header required) | GA |
| Platform Support | Full | Direct API only | Full |

#### 2. Primary Use Cases Identified

**OpenAI Files API:**
- Fine-tuning with JSONL files
- Assistants API with document retrieval
- Batch processing workflows
- Vector stores for RAG implementation
- Vision model training

**Anthropic Files API:**
- Code execution tool integration
- Persistent document storage
- Multi-session document analysis
- MCP connector workflows

**Google Gemini Files API:**
- Large media file processing (video, audio)
- Multimodal content generation
- Temporary file handling for one-off operations

#### 3. W3C File API - Browser Technology

**Core Interfaces:**
- `File`: Represents file data from user's system
- `Blob`: Binary Large Object for raw data
- `FileReader`: Async reading interface
- `FileList`: Collection of File objects

**Key Methods:**
- `readAsArrayBuffer()`: For binary processing
- `readAsText()`: For text content
- `readAsDataURL()`: For base64-encoded data URLs

**Browser Support:**
- 97/100 compatibility score
- Full support in all modern browsers
- IE 10-11 partial support only

#### 4. File System Access API (Advanced Browser API)

- Enables read/write to local files
- Requires explicit user permission
- Chromium-only (Chrome, Edge)
- NOT supported in Firefox/Safari
- Persistent permissions in Chrome 122+

### Important Technical Details

#### OpenAI API Endpoints
```
POST   /v1/files              - Upload file
GET    /v1/files              - List files
GET    /v1/files/{id}         - Get file details
GET    /v1/files/{id}/content - Download content
DELETE /v1/files/{id}         - Delete file
```

#### Anthropic Beta Headers
```
Files API:        anthropic-beta: files-api-2025-04-14
Code Execution:   anthropic-beta: code-execution-2025-08-25
Combined:         anthropic-beta: code-execution-2025-08-25,files-api-2025-04-14
```

#### Gemini File Limitations
- Files auto-delete after 48 hours
- Workaround: Cron job to re-upload every 24 hours
- Cannot download files during storage period (metadata only)

### Market Context

- Enterprise LLM spend 2025: Anthropic 40%, OpenAI 27%, Google 21%
- Shift from OpenAI dominance (was 50% in 2023)
- Price competition intensifying
- Long-context and file handling becoming differentiators

### Security Considerations

- All providers use encryption at rest and in transit
- Files scoped to workspace/organization
- GDPR compliance requires careful data handling
- No cross-workspace file sharing by default

### Gaps Identified for Further Research

1. Detailed pricing breakdown for file storage (separate from token costs)
2. Performance benchmarks for large file processing
3. Comparison of document parsing accuracy
4. Integration patterns with existing workflows
5. Self-hosted alternatives comparison

### Visual Assets Needed

- [ ] Comparison table graphic
- [ ] Architecture diagram for each provider
- [ ] File upload flow diagrams
- [ ] Browser API compatibility matrix
- [ ] Market share visualization

---

*Notes compiled: January 9, 2026*
