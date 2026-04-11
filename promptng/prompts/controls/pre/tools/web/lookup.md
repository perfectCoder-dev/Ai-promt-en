# 🌐 Tool: web_lookup

Retrieve up-to-date or external information from the web.

---

## 🧠 Purpose

This tool allows the model to access information beyond its training data by querying external web sources.

It is essential for:
- Real-time data
- Fact-checking
- Unknown or dynamic information

---

## ✅ When To Use

Use this tool if:

- The user asks for **current or recent information**
- The answer depends on **external knowledge**
- The model is **uncertain or lacks confidence**
- Verification from external sources is needed

---

## 🚫 When NOT To Use

Do NOT use this tool if:

- The answer is already known and stable
- The question is purely conceptual or opinion-based
- The user explicitly forbids external access

---

## 📥 Input

| Name   | Type   | Required | Description        |
|--------|--------|----------|--------------------|
| query  | string | yes      | Search query       |

---

## 📤 Output

- Text summary of results  
- Or raw retrieved content  

---

## ⚖️ Rules

- Prefer **concise and specific queries**
- Do **not fabricate results**
- If the tool fails, **acknowledge uncertainty**
- Base final answers **only on retrieved data**
- Do not hallucinate sources

---

## 🧪 Examples

### Example 1

```json
{
  "query": "population of Costa Rica 2026"
}
```

### Example 2

```json
{
  "query": "latest news about AI regulation Europe"
}
```
