# Research Notes: File Upload & Retrieval API Comparison
## OpenAI vs Google Gemini vs Anthropic

---

## OpenAI Files API

### File Size Limits
- **Assistants/GPT**: 512MB per file, 2M tokens per file
- **Fine-tuning**: 1GB max, JSONL format only
- **Vision**: 20MB max for images
- **Batch**: 100MB max, JSONL format
- **Uploads API**: Up to 8GB total (64MB parts)

### Supported File Purposes
1. `assistants` - Used in Assistants API
2. `assistants_output` - Output from Assistants
3. `batch` - Used in Batch API
4. `batch_output` - Output from Batch
5. `fine-tune` - For fine-tuning models
6. `fine-tune-results` - Fine-tuning results
7. `vision` - Images for vision fine-tuning
8. `user_data` - Flexible file type for any purpose
9. `evals` - Used for evaluation datasets

### Supported File Formats

**Documents (File Search)**:
- PDF, TXT, DOCX, MD, HTML
- PPTX, XLSX, CSV, JSON
- Code files: JS, PY, etc.

**Images (Vision)**:
- PNG, JPEG, GIF, WebP

**Data (Fine-tuning)**:
- JSONL only

### Retention Policy
- Batch files: Auto-expire after 30 days
- All other files: Persist until manually deleted
- No automatic cleanup except batch

### Assistant Limits
- Max 20 files per assistant
- 512MB each, 5M tokens per file
- **DEPRECATED**: Assistants API shuts down August 26, 2026
- Replacement: Responses API

### Known Issues (Community Reports)
- CSV uploads sometimes fail despite being listed as supported
- Documentation lacks clear comprehensive format list
- Some formats work in one context but not another

---

## Google Gemini Files API

### File Size Limits
- **Per file**: 2GB (recently increased to 5GB)
- **Per project**: 20GB (recently increased to 50GB)
- **Inline uploads**: <20MB (included in request body)
- **PDFs**: 50MB or 1000 pages max
- **Videos**: Up to 2GB per video

### Upload Methods
1. **Inline Data**: For files <20MB, base64 in request
2. **Files API (media.upload)**: For larger files
   - Upload file, get file reference
   - Use reference in generation requests

### Supported File Formats

**Documents**:
- PDF (primary, uses vision)
- DOCX, TXT
- XLSX, CSV

**Images**:
- PNG, JPEG, GIF, WebP

**Audio** (added 2025):
- MP3, M4A, WAV
- 10 minutes cap (3 hours Pro/Ultra)

**Video**:
- Various formats
- 5 minutes cap (1 hour Pro/Ultra)

### Retention Policy
- **48 hours automatic deletion**
- No manual download available
- Files purge automatically after 48h
- Workaround: Re-upload via cron job every 24h

### Pricing
- **Storage: FREE** in all regions
- Only processing (inference) costs money
- Generally lower than OpenAI pricing

### PDF Processing
- Uses native vision to understand documents
- Processes text, images, diagrams, charts, tables
- Each page = ~258 tokens
- PDF pages treated as images internally

### Enterprise Features
- Regional storage selection (US, EU, APAC)
- Compliance-ready data residency

### Known Issues
- 48h retention forces re-uploads for persistent use
- 20GB quota can fill quickly with video processing
- No way to extend retention period (feature request)

---

## Anthropic Claude Files API

### API Status
- **Currently in BETA**
- Requires header: `anthropic-beta: files-api-2025-04-14`
- Endpoint: `POST https://api.anthropic.com/v1/files`

### File Size Limits
- **Per file**: 500MB (350MB in some sources)
- **Per organization**: 100GB storage
- **PDFs**: 32MB max, 100 pages max
- **Images**: 8000x8000px max single image
- **20+ images**: 2000x2000px limit applies

### Supported File Formats

**Documents**:
- PDF (converted to images per page)
- DOCX (convert to PDF for image parsing)
- TXT, CSV, XLSX
- Markdown

**Images**:
- JPEG, PNG, GIF, WebP
- Optimal: 1.15 megapixels, 1568px dimensions
- Token cost: (width × height) / 750

### Upload Methods
1. **Direct base64**: Include in request body
2. **URL reference**: Provide image URL
3. **Files API (beta)**: Upload once, get file_id
   - Reference via `{"type": "file", "file_id": "..."}`

### File Reference System
- Upload → receive `file_id`
- Use `file_id` in document content blocks
- "Create once, use many times" pattern
- Supports list, retrieve, delete operations

### Retention Policy
- Configurable: 0-365 days (enterprise/tenant)
- More flexible than competitors

### PDF Processing
- Converts each page to image
- Enables visual understanding
- Works with citations feature
- Compatible with prompt caching and batch processing

### Image Processing
- Up to 100 images per API request
- 5 images per turn on claude.ai web
- Images before text = best results

### Platform Availability
- **NOT available** on Amazon Bedrock
- **NOT available** on Google Vertex AI
- Direct API only

### Model Support
- Images: All Claude 3+ models
- PDFs: All Claude 3.5+ models
- Other files (code exec): Claude Haiku 4.5+, Claude 3.7+

---

## Comparison Summary

| Feature | OpenAI | Gemini | Anthropic |
|---------|--------|--------|-----------|
| Max File Size | 512MB (8GB Uploads API) | 2-5GB | 500MB |
| Storage Limit | Per-file limits | 20-50GB/project | 100GB/org |
| Retention | Permanent (manual delete) | 48 hours auto | 0-365 days config |
| PDF Support | Yes | Yes (vision) | Yes (vision) |
| Image Support | Yes | Yes | Yes |
| Audio Support | Whisper API | Yes | No |
| Video Support | No direct | Yes | No |
| Free Storage | No | Yes | Unknown |
| API Status | Deprecated (Responses API) | Stable | Beta |

---

## Key Differentiators

### OpenAI
- Most mature ecosystem
- Assistants API being deprecated
- Purpose-based file handling
- Permanent storage until deletion

### Google Gemini
- Largest context window (1M tokens)
- Native multimodal (audio, video)
- FREE file storage
- 48h auto-deletion limits persistence

### Anthropic
- Beta but feature-rich
- Flexible retention (0-365 days)
- Large org storage (100GB)
- Vision-based PDF processing
- Not available on cloud marketplaces

---

*Notes compiled: January 10, 2025*
