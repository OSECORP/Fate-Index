# Cloudflare Pages Deployment Configuration

## Overview

This directory is configured for deployment on **Cloudflare Pages**.

### Key Files

- **_headers** — CORS and security headers configuration
- **web_interface/index.html** — SIGMA PRIME 4.0 visualization (public entry point)
- **docs/** — Technical documentation
- **src/** — Core computation engine

### Deployment Steps

1. Connect GitHub repository to Cloudflare Pages
2. Build command: `npm install` (if needed) or leave blank for static files
3. Publish directory: `/` (root)
4. Framework: None (static site)

### Accessing SIGMA PRIME 4.0

After deployment:
```
https://[your-cloudflare-domain]/web_interface/index.html
```

Or on custom domain:
```
https://nonilliard.net/web_interface/index.html
```

### CORS Configuration

The `_headers` file automatically configures:
- **Access-Control-Allow-Origin**: `*` (allows cross-origin requests)
- **Access-Control-Allow-Methods**: GET, POST, OPTIONS
- **Access-Control-Allow-Headers**: `*`
- **Cache-Control**: Optimized for static assets
- **Security headers**: nosniff, SAMEORIGIN, referrer policy

### Verification

After deployment, verify CORS headers:
```bash
curl -I https://[your-domain]/web_interface/index.html
```

Expected response headers:
```
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: *
```

✅ If present, SIGMA PRIME 4.0 will render correctly.

### Directory Structure

```
Fate-Index/
├── _headers (← Cloudflare Pages config)
├── CLOUDFLARE_DEPLOYMENT.md (← this file)
├── web_interface/
│   └── index.html (← SIGMA PRIME 4.0 entry point)
├── docs/
├── src/
└── README.md
```

### Troubleshooting

**Issue**: A-Frame not loading (blank page)
- **Solution**: Check `_headers` is present in root
- **Verify**: `curl -I` shows CORS headers

**Issue**: Fonts not loading
- **Solution**: CORS headers allow CDN resources
- **Verify**: Browser console shows no CORS errors

**Issue**: 3D scene not rendering
- **Solution**: Clear browser cache and reload
- **Verify**: Open DevTools → Network tab → all resources loaded ✅

---

**Status**: ✅ Ready for Cloudflare Pages deployment

**Last Updated**: 2026-07-16

**Maintainer**: OSECORP
