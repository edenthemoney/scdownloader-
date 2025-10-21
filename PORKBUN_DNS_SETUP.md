# 🐷 Porkbun DNS Setup for Ezoic Verification

## Step-by-Step Instructions for Porkbun

### Step 1: Log In to Porkbun

1. Go to: https://porkbun.com/
2. Click **"Sign In"** (top right)
3. Enter your email and password
4. Log in

---

### Step 2: Access Domain Management

1. After logging in, you'll see your **Account Dashboard**
2. Look for **"Domain Management"** or your domain list
3. Find: `soundcloudfreeplaylistdownloader.xyz`
4. Click on the domain name or click **"Details"** button

---

### Step 3: Go to DNS Records

1. On the domain details page, look for tabs or sections
2. Click **"DNS"** or **"DNS Records"** tab
3. You should see existing DNS records (if any)

---

### Step 4: Add TXT Record

1. Look for **"Add"** or **"Add Record"** button
2. Click it
3. You'll see a form to add a new DNS record

**Fill in the form:**

| Field | Value |
|-------|-------|
| **Type** | Select **TXT** from dropdown |
| **Host** | Enter `@` or leave blank |
| **Answer** | Paste your Ezoic verification code |
| **TTL** | Leave default (usually 600 or Auto) |
| **Priority** | Leave blank (not needed for TXT) |

**Example:**
```
Type: TXT
Host: @
Answer: ezoic-site-verification=abc123xyz456...
TTL: 600
```

4. Click **"Add"** or **"Save"** button

---

### Step 5: Verify the Record Was Added

After saving, you should see your new TXT record in the list:

```
Type: TXT
Name: @ or soundcloudfreeplaylistdownloader.xyz
Content: ezoic-site-verification=abc123xyz...
```

✅ If you see it, you're done with Porkbun!

---

### Step 6: Wait for DNS Propagation

**Time needed:** Usually 5-15 minutes with Porkbun (they're pretty fast!)

**What's happening:**
- Porkbun updates their DNS servers
- Changes propagate across the internet
- Ezoic can then verify your domain

---

### Step 7: Check if DNS Propagated (Optional)

While waiting, you can check if it's ready:

1. Go to: https://dnschecker.org/
2. Enter: `soundcloudfreeplaylistdownloader.xyz`
3. Select: **TXT** from dropdown
4. Click **"Search"**
5. Should show your Ezoic verification code

**If you see it:** DNS is propagated! ✅  
**If you don't:** Wait 5-10 more minutes

---

### Step 8: Verify in Ezoic

1. Go back to **Ezoic dashboard**
2. Find the verification page
3. Click **"Verify"** button
4. Should see: ✅ **"Domain verified successfully!"**

**If verification fails:**
- Wait another 10 minutes
- Try clicking "Verify" again
- DNS might still be propagating

---

## 🎯 Porkbun-Specific Tips

### Porkbun is Fast!
- Porkbun typically propagates DNS changes in 5-15 minutes
- Much faster than some other registrars
- You can usually verify within 15-20 minutes

### Default TTL is Fine
- Porkbun's default TTL (600 seconds = 10 minutes) is perfect
- No need to change it

### Host Field Options
- You can use `@` 
- Or leave it blank
- Or use your full domain name
- All work the same in Porkbun

---

## 📸 Visual Guide

### What You'll See in Porkbun:

**DNS Records Page:**
```
┌─────────────────────────────────────────────────┐
│  DNS Records for soundcloudfreeplaylist...      │
│                                                  │
│  [Add Record]                                   │
│                                                  │
│  Type    Host    Answer              TTL        │
│  ─────────────────────────────────────────────  │
│  A       @       123.45.67.89        600        │
│  TXT     @       ezoic-site-verif... 600   ← NEW│
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## ⚠️ Troubleshooting

### "Can't find DNS section"

**Solution:**
1. Make sure you clicked on the domain name
2. Look for tabs: Overview, DNS, Nameservers, etc.
3. Click **"DNS"** tab
4. Should see DNS records

### "Verification failed in Ezoic"

**Possible reasons:**
1. **Too soon** → Wait 10 more minutes
2. **Wrong TXT value** → Check you copied it correctly
3. **Wrong host** → Try using `@` instead of blank

### "Don't see Add Record button"

**Solution:**
- Scroll down on the DNS page
- Button might be at the bottom
- Or look for "+ Add" or "New Record"

---

## ✅ After Verification Success

Once Ezoic shows "Domain verified":

1. ✅ Continue with Ezoic setup
2. ✅ Enable Ad Tester
3. ✅ Configure ad settings
4. ✅ Go live with ads

**I've already added Ezoic code to your site**, so ads will start showing within 1-2 hours after you complete setup!

---

## 🚀 Quick Summary

1. **Log in to Porkbun** → https://porkbun.com/
2. **Go to your domain** → soundcloudfreeplaylistdownloader.xyz
3. **Click DNS tab**
4. **Add TXT record:**
   - Type: TXT
   - Host: @
   - Answer: [Ezoic verification code]
5. **Save**
6. **Wait 15 minutes**
7. **Verify in Ezoic** → Click "Verify" button
8. **Done!** ✅

---

## ⏰ Timeline

- **Now:** Add TXT record in Porkbun
- **+5 min:** DNS starts propagating
- **+15 min:** DNS fully propagated
- **+20 min:** Click "Verify" in Ezoic
- **+25 min:** Domain verified ✅
- **+30 min:** Complete Ezoic setup
- **+1-2 hours:** Ezoic ads start showing

---

**Need help?** Let me know if you:
- Can't find the DNS section
- Get any error messages
- Verification fails

I'm here to help! 🎯
