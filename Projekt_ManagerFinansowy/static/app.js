const userId = "user_1"; // domyślny user_id

document.getElementById("exchangeBtn").addEventListener("click", exchangeToken);
document.getElementById("refreshTokensBtn").addEventListener("click", fetchTokens);
document.getElementById("loadAccountsBtn").addEventListener("click", fetchAccounts);
document.getElementById("loadTransactionsBtn").addEventListener("click", fetchTransactions);

async function exchangeToken() {
  const token = document.getElementById("publicTokenInput").value;
  if (!token) return alert("Wklej public_token!");

  try {
    const res = await fetch(`/api/item/public_token/exchange?user_id=${userId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ public_token: token })
    });
    const data = await res.json();
    document.getElementById("exchangeResult").innerText = JSON.stringify(data, null, 2);
    fetchTokens();
  } catch (err) {
    console.error(err);
  }
}

async function fetchTokens() {
  try {
    const res = await fetch(`/api/token?user_id=${userId}`);
    const data = await res.json();
    document.getElementById("tokensDisplay").innerText = JSON.stringify(data, null, 2);
  } catch (err) {
    console.error(err);
  }
}

async function fetchAccounts() {
  try {
    const res = await fetch(`/api/accounts?user_id=${userId}`);
    const data = await res.json();
    document.getElementById("accountsDisplay").innerText = JSON.stringify(data, null, 2);
  } catch (err) {
    console.error(err);
  }
}

async function fetchTransactions() {
  try {
    const res = await fetch(`/api/transactions?user_id=${userId}`);
    const data = await res.json();
    document.getElementById("transactionsDisplay").innerText = JSON.stringify(data, null, 2);
  } catch (err) {
    console.error(err);
  }
}

// Auto-load tokens przy starcie
fetchTokens()