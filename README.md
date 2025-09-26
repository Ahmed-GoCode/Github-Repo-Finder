# GitHub Search Telegram Bot 🤖

<div align="center">
  <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Made%20with-❤️-red.svg?style=for-the-badge" alt="Made with Love">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge" alt="PRs Welcome">
</div>

A Telegram bot that allows users to search GitHub repositories directly from Telegram chat. Built with Python using the PyTelegramBotAPI library and GitHub API.

## Features ✨

- 🔍 **Search GitHub repositories** by keyword
- 📄 **Paginated results** (5 results per page)
- ⭐ **Display repository information** including name, description, stars, and URL
- 🎯 **Interactive navigation** with Previous/Next buttons
- ⚡ **Real-time API integration** with GitHub
- 🛡️ **Error handling** for API rate limits and network issues

## Prerequisites 📋

Before running the bot, make sure you have:

- Python 3.6 or higher
- A Telegram Bot Token (get it from [@BotFather](https://t.me/BotFather))
- Internet connection for GitHub API access

## Installation 🚀

1. **Clone or download** this repository
2. **Install required packages**:
   ```bash
   pip install pyTelegramBotAPI requests
   ```

## Usage 💡

1. **Run the bot**:
   ```bash
   python github.py
   ```

2. **Enter your Bot Token** when prompted

3. **Start using the bot** in Telegram:
   - Send `/start` to get welcome message
   - Send any keyword to search GitHub repositories
   - Use navigation buttons to browse through results

## Bot Commands 📝

- `/start` - Display welcome message and instructions

## How It Works 🔧

1. User sends a search query to the bot
2. Bot makes a request to GitHub API: `https://api.github.com/search/repositories`
3. Results are formatted and displayed with pagination
4. Users can navigate through pages using inline buttons
5. Each result shows:
   - Repository name
   - Star count
   - Description (truncated if too long)
   - Direct link to repository


## Error Handling 🛠️

The bot handles various error scenarios:

- **Rate Limit Exceeded** (403) - GitHub API limits
- **Invalid Query** (422) - Malformed search terms
- **Timeout Errors** - Network timeouts
- **Connection Errors** - Internet connectivity issues
- **General API Errors** - Other HTTP status codes

## API Limitations ⚠️

- GitHub API has rate limiting (60 requests per hour for unauthenticated requests)
- Search results are limited to what GitHub API returns
- No authentication implemented (uses public access)

## Configuration 🔧

The bot can be customized by modifying these parameters:

- **Results per page**: Currently set to 5 (line 25)
- **Description length**: Truncated at 100 characters (line 29)
- **Request timeout**: Set to 10 seconds (line 86)

## Dependencies 📦

```
pyTelegramBotAPI>=4.0.0
requests>=2.25.0
```

## Future Enhancements 🚀

Potential improvements:
- GitHub authentication for higher rate limits
- Repository filtering options
- Save favorite repositories
- Direct repository download links
- Repository statistics and insights

## Contributing 🤝

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## ⭐ Show Your Support

If you found this project helpful, please give it a ⭐ star on GitHub!

---

<div align="center">
  <p>Made with ❤️ by <strong>Ahmad</strong></p>
  <img src="https://img.shields.io/badge/Developer-Ahmad-blue.svg?style=for-the-badge" alt="Developer Ahmad">
</div>
