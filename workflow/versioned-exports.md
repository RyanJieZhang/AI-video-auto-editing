# Versioned Exports

High-quality videos are rarely finished in one export. Use version folders so every draft can be compared.

## Folder Pattern

```text
exports/
├── v001/
│   ├── video.mp4
│   ├── quality-review.md
│   ├── packaging.md
│   └── manifest.md
├── v002/
└── v003/
```

## Create A Version

Use:

```powershell
C:\Users\1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts/create_export_version.py exports/your-video.mp4
```

Optional:

```powershell
C:\Users\1\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe scripts/create_export_version.py exports/your-video.mp4 --name v002 --notes plan/edit-decision-list.md plan/lookbook.md
```

## Review Each Version

For every version, answer:

- Is the hook stronger than the previous version?
- Is the story clearer?
- Are weak shots removed?
- Is the visual style more consistent?
- Is audio clearer?
- Did the quality score improve?

Do not overwrite exports when comparing creative direction or edit quality.
