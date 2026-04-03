*🌍 Leer esto en [Español](setup-ssh-github.md)*

# 🔐 Setup Github SSH for your Repository

If you created a new GitHub account, or if you want to push your repository seamlessly without being prompted for passwords or tokens every time, follow this guide to set up an SSH Key connection.

---

## 1. Generate a new SSH Key

Open your terminal and run the following command, replacing the email with your GitHub linked address:

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

1. It will prompt `Enter a file in which to save the key`. Press **Enter** to accept the default path (`/home/user/.ssh/id_ed25519`).
2. It will ask for a `passphrase`. You can enter a secure password or leave it blank (press **Enter** twice) for automated pushes.

## 2. Start the SSH Agent

Activate the ssh-agent in the background:

```bash
eval "$(ssh-agent -s)"
```

Add your newly created private key:

```bash
ssh-add ~/.ssh/id_ed25519
```

## 3. Add the public key to GitHub

We need to copy the contents of the public file.

Print the key into your terminal:

```bash
cat ~/.ssh/id_ed25519.pub
```

Copy the entire output string (starting with `ssh-ed25519...`).

**In Github:**
1. Navigate to **Settings** (Profile settings on the top right corner).
2. Click on **SSH and GPG keys** in the left sidebar.
3. Click the green button **New SSH key**.
4. Give it an identifiable Title, eg: "My Local Server".
5. Paste the copied string into the "Key" text area and click **Add SSH key**.

## 4. Test the connection

Run this to verify you are correctly authenticated:

```bash
ssh -T git@github.com
```

You may be prompted: `Are you sure you want to continue connecting (yes/no/[fingerprint])?`. Type **yes** and hit Enter.

You should receive a successful greeting: `Hi USERNAME! You've successfully authenticated...`

---

## 5. Push out the project (`selfhosted-n8n-ai-stack`)

Now that SSH is configured, let's initialize Git and push the stack up.

Ensure you are inside the repository root directory:

```bash
cd /path/to/selfhosted-n8n-ai-stack
```

Initialize Git:

```bash
git init
```

Stage all files (the `.gitignore` is already protecting secrets automatically) and make the first commit:

```bash
git add .
git commit -m "🚀 Initial commit: Self-hosted n8n AI stack full configuration"
```

Link your remote GitHub repository as the origin (replace the URL with yours):

```bash
git remote add origin git@github.com:USERNAME/selfhosted-n8n-ai-stack.git
```

Rename the primary branch structure to `main`:

```bash
git branch -M main
```

Push everything natively to GitHub!

```bash
git push -u origin main
```

And you're done! Your entire AI architecture is now open sourced and pushed via SSH successfully.
