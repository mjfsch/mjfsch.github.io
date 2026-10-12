"use strict";

// This script only enhances copying. All content and links work without it.
const button = document.getElementById("copy-username");
const username = document.getElementById("discord-username");
const label = document.getElementById("copy-label");
const status = document.getElementById("copy-status");
let resetTimer;

button.hidden = false;
button.addEventListener("click", async () => {
  clearTimeout(resetTimer);
  // Discord's Add Friend field expects the username without the display @.
  const value = username.textContent.trim().replace(/^@/, "");
  try {
    if (!navigator.clipboard || !window.isSecureContext) {
      throw new Error("Clipboard unavailable");
    }
    await navigator.clipboard.writeText(value);
    label.textContent = "Copied";
    status.textContent = `${value} copied. Paste it into Discord's Add Friend field.`;
    resetTimer = setTimeout(() => { label.textContent = "Copy"; }, 4000);
  } catch {
    // Leave a selectable username and useful instructions when permission fails.
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(username);
    selection.removeAllRanges();
    selection.addRange(range);
    label.textContent = "Copy";
    status.textContent = `Copy wasn't available. Select ${value} above, or type it into Discord's Add Friend field.`;
  }
});
