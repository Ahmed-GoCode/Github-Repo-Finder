import telebot
import requests
from urllib.parse import quote_plus
from telebot import types

bot = telebot.TeleBot(input('[÷] YouR ToKeN BoT ==> '))

user_search_data = {}

def AK(user_id, current_page, total_pages):
    keyboard = types.InlineKeyboardMarkup()
    buttons = []
    
    if current_page > 1:
        buttons.append(types.InlineKeyboardButton("⬅️ Previous", callback_data=f"prev_{user_id}_{current_page-1}"))
    
    if current_page < total_pages:
        buttons.append(types.InlineKeyboardButton("➡️ Next", callback_data=f"next_{user_id}_{current_page+1}"))
    
    if buttons:
        keyboard.row(*buttons)
    
    return keyboard

def AHMD(projects, query, page, total_pages):
    result_texts = []
    start_idx = (page - 1) * 5
    end_idx = min(start_idx + 5, len(projects))
    
    for i, project in enumerate(projects[start_idx:end_idx], start_idx + 1):
        project_name = project['name']
        project_url = project['html_url']
        description = project.get('description', 'No description')
        if len(description) > 100:
            description = description[:100] + '...'
        stars = project.get('stargazers_count', 0)
        result_texts.append(f"🔍 Result {i}:\n📁 {project_name}\n⭐ {stars} stars\n📝 {description}\n🔗 {project_url}\n{'='*30}")
    
    response_text = f"✅ Found {len(projects)} repositories for '{query}'\n📄 Page {page}/{total_pages}\n\n" + '\n\n'.join(result_texts)
    return response_text
@bot.message_handler(commands=['start'])
def HMD(message):
    bot.reply_to(message, '''👋 Welcome!

🔍 This bot searches GitHub repositories for you.
📝 Simply send me any search term and I'll find related projects.

                 🚀 Try sending a keyword to get started!''')

@bot.callback_query_handler(func=lambda call: True)
def HMOUDI(call):
    try:
        data_parts = call.data.split('_')
        action = data_parts[0]  
        user_id = int(data_parts[1])
        new_page = int(data_parts[2])
        
        if user_id in user_search_data:
            search_info = user_search_data[user_id]
            projects = search_info['projects']
            query = search_info['query']
            total_pages = search_info['total_pages']
            
            user_search_data[user_id]['current_page'] = new_page
            
            response_text = AHMD(projects, query, new_page, total_pages)
            
            keyboard = AK(user_id, new_page, total_pages)
            
            bot.edit_message_text(
                text=response_text,
                chat_id=call.message.chat.id,
                message_id=call.message.message_id,
                reply_markup=keyboard
            )
            
        bot.answer_callback_query(call.id)
        
    except Exception as e:
        bot.answer_callback_query(call.id, f"Error: {str(e)}")

@bot.message_handler(func=lambda message: True)
def AKsearch_github_projects(message):
    query = message.text
    user_id = message.from_user.id
    encoded_query = quote_plus(query)
    search_url = f"https://api.github.com/search/repositories?q={encoded_query}"
    
    try:
        response = requests.get(search_url, timeout=10)
        
        if response.status_code == 200:
            projects = response.json().get('items', [])
            if projects:
                total_pages = (len(projects) + 4) // 5
                current_page = 1
                
                user_search_data[user_id] = {
                    'projects': projects,
                    'query': query,
                    'current_page': current_page,
                    'total_pages': total_pages
                }
                
                response_text = AHMD(projects, query, current_page, total_pages)
                
                keyboard = AK(user_id, current_page, total_pages)
                
                bot.reply_to(message, response_text, reply_markup=keyboard)
            else:
                bot.reply_to(message, f"🚫 No repositories found for '{query}'")
        elif response.status_code == 403:
            bot.reply_to(message, "❌ GitHub API rate limit exceeded. Please try again later.")
        elif response.status_code == 422:
            bot.reply_to(message, f"❌ Invalid search query: '{query}'. Please try a different search term.")
        else:
            bot.reply_to(message, f"❌ GitHub API error (Status: {response.status_code}). Please try again.")
            
    except requests.exceptions.Timeout:
        bot.reply_to(message, "⏰ Request timeout. Please try again.")
    except requests.exceptions.ConnectionError:
        bot.reply_to(message, "🌐 Connection error. Please check your internet connection.")
    except requests.exceptions.RequestException as e:
        bot.reply_to(message, f"❌ Network error: {str(e)}")
    except Exception as e:
        bot.reply_to(message, f"❌ Unexpected error: {str(e)}")
bot.polling()
