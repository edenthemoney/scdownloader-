# 🔐 Ezoic DNS Verification Guide

## What You Need to Do

Ezoic needs to verify you own `soundcloudfreeplaylistdownloader.xyz` by adding a DNS TXT record.

---

## 📋 Step-by-Step Instructions

### Step 1: Get Your TXT Record from Ezoic

In the Ezoic dashboard, you should see a TXT record that looks like:

```
ezoic-site-verification=abc123xyz456...
```

**Copy this entire value** (it's unique to your account)

---

### Step 2: Find Your Domain Registrar

Where did you buy your domain `soundcloudfreeplaylistdownloader.xyz`?

Common registrars:
- **Namecheap** (namecheap.com)
- **GoDaddy** (godaddy.com)
- **Google Domains** (domains.google.com)
- **Cloudflare** (cloudflare.com)
- **Render** (if you bought through them)
- **Other**

**You need to log in to wherever you bought the domain.**

---

### Step 3: Add TXT Record (Instructions by Provider)

#### **If Using Namecheap:**

1. Log in to Namecheap
2. Go to **Domain List**
3. Click **Manage** next to your domain
4. Click **Advanced DNS** tab
5. Click **Add New Record**
6. Select **TXT Record**
7. Fill in:
   - **Host:** `@` (or leave blank)
   - **Value:** Paste the Ezoic verification code
   - **TTL:** Automatic (or 1 min)
8. Click **Save**

---

#### **If Using GoDaddy:**

1. Log in to GoDaddy
2. Go to **My Products**
3. Click **DNS** next to your domain
4. Click **Add** button
5. Select **TXT** from dropdown
6. Fill in:
   - **Name:** `@`
   - **Value:** Paste the Ezoic verification code
   - **TTL:** 1 Hour (or default)
7. Click **Save**

---

#### **If Using Cloudflare:**

1. Log in to Cloudflare
2. Select your domain
3. Click **DNS** in the sidebar
4. Click **Add record**
5. Fill in:
   - **Type:** TXT
   - **Name:** `@`
   - **Content:** Paste the Ezoic verification code
   - **TTL:** Auto
6. Click **Save**

---

#### **If Using Google Domains:**

1. Log in to Google Domains
2. Click on your domain
3. Click **DNS** in the left menu
4. Scroll to **Custom resource records**
5. Fill in:
   - **Name:** `@` (or leave blank)
   - **Type:** TXT
   - **TTL:** 1H
   - **Data:** Paste the Ezoic verification code
6. Click **Add**

---

#### **If Using Render or Other Host:**

1. Log in to your hosting provider
2. Find **DNS Settings** or **DNS Management**
3. Add a **TXT record**
4. Use:
   - **Host/Name:** `@` or blank or `soundcloudfreeplaylistdownloader.xyz`
   - **Value/Content:** Paste the Ezoic verification code
   - **TTL:** Lowest available (1 min or auto)
5. Save

---

### Step 4: Wait for Propagation

**Time needed:** Usually 5-15 minutes, but can take up to 72 hours

**How to check if it's ready:**
1. Go to: https://dnschecker.org/
2. Enter your domain: `soundcloudfreeplaylistdownloader.xyz`
3. Select **TXT** from dropdown
4. Click **Search**
5. Should show your Ezoic verification code

---

### Step 5: Verify in Ezoic

1. Go back to Ezoic dashboard
2. Click **"Verify"** button
3. If successful: ✅ "Domain verified!"
4. If not ready: Wait 10 more minutes and try again

---

## 🔍 Troubleshooting

### "Verification failed"

**Possible reasons:**
1. **DNS not propagated yet** → Wait 10-30 minutes
2. **Wrong TXT value** → Double-check you copied it correctly
3. **Wrong host field** → Try `@` or blank or full domain
4. **TTL too high** → Set to lowest available

### "Can't find DNS settings"

**Solution:**
- Contact your domain registrar support
- Tell them: "I need to add a TXT record for domain verification"
- They'll guide you to the right place

### "Don't remember where I bought domain"

**How to find out:**
1. Go to: https://whois.domaintools.com/
2. Enter: `soundcloudfreeplaylistdownloader.xyz`
3. Look for **Registrar** field
4. That's where you bought it

---

## 📝 Example TXT Record

**What Ezoic gives you:**
```
ezoic-site-verification=abc123xyz456def789ghi012jkl345mno678pqr901stu234
```

**What you add to DNS:**
- **Type:** TXT
- **Host:** `@`
- **Value:** `ezoic-site-verification=abc123xyz456def789ghi012jkl345mno678pqr901stu234`
- **TTL:** Auto or 1 min

---

## ⏰ Timeline

- **Now:** Add TXT record
- **5-15 min:** DNS propagates
- **15-20 min:** Click "Verify" in Ezoic
- **20-25 min:** Domain verified ✅
- **25-30 min:** Continue Ezoic setup
- **1-2 hours:** Ezoic ads start showing

---

## ✅ After Verification

Once verified, Ezoic will:
1. ✅ Confirm domain ownership
2. ✅ Allow you to continue setup
3. ✅ Enable ad integration
4. ✅ Start showing ads on your site

---

## 🚀 Next Steps After Verification

1. **Complete Ezoic setup**
2. **Enable Ad Tester**
3. **Configure ad settings**
4. **Go live with ads**

I've already added the Ezoic code to your site, so once verified, ads will start showing automatically!

---

## 💡 Quick Reference

**What you need:**
- Ezoic TXT verification code (from Ezoic dashboard)
- Access to your domain registrar
- 15-30 minutes for DNS propagation

**Where to add:**
- Your domain registrar's DNS settings
- Add as TXT record
- Host: `@`
- Value: Ezoic verification code

**How to verify:**
- Wait 15 minutes
- Click "Verify" in Ezoic
- Should see success message

---

**Need help?** Tell me:
1. Where you bought your domain
2. If you can access DNS settings
3. Any error messages you see

I'll guide you through it! 🎯
