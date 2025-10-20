#!/bin/bash

# Deploy AdSense fixes to production

echo "🚀 Deploying AdSense fixes..."
echo ""

# Add all changes
echo "📦 Adding files..."
git add app.py
git add templates/adsense-diagnostic.html
git add ADSENSE_72_HOUR_FIX.md
git add DEPLOY_FIX_NOW.md
git add HOW_TO_ADD_SITE_ADSENSE.md
git add QUICK_FIX_CHECKLIST.md

# Commit
echo "💾 Committing changes..."
git commit -m "Fix ads.txt 404 error and add comprehensive AdSense diagnostic tools"

# Push
echo "🌐 Pushing to production..."
git push origin main

echo ""
echo "✅ Deployment complete!"
echo ""
echo "⏰ Wait 2-3 minutes for your hosting provider to rebuild and deploy."
echo ""
echo "🧪 Then test these URLs:"
echo "   1. https://soundcloudfreeplaylistdownloader.xyz/ads.txt"
echo "   2. https://soundcloudfreeplaylistdownloader.xyz/adsense-diagnostic"
echo ""
echo "📋 Next steps:"
echo "   1. Verify ads.txt is accessible (should show your publisher ID)"
echo "   2. Visit the diagnostic page to check status"
echo "   3. Add your site to AdSense: https://www.google.com/adsense/new/u/0/sites"
echo ""
