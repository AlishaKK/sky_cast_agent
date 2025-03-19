

```
# Weather Agent 🌦️  

A chatbot assistant that provides real-time weather updates using Chainlit, OpenAI Agents, and OpenWeatherMap API.  

## 🚀 Features  
- Fetches live weather data for any city  
- Uses OpenAI Agents for AI interactions  
- Built with Chainlit for an interactive chat experience  

## 🛠 Installation  

### 1️⃣ Set up the project  
```bash
uv init --package weather_agent
cd weather_agent
```

### 2️⃣ Install dependencies  
```bash
uv add chainlit
uv add openai-agents
uv add python-dotenv
uv add requests
uv sync
```

### 3️⃣ Configure environment variables  
Create a `.env` file in the project root and add:  
```
GEMINI_API_KEY=your_gemini_api_key
WEATHER_API_KEY=your_openweather_api_key
```

### 4️⃣ Run the chatbot  
```bash
uv run dev
```

## 📌 Usage  
- Start the chatbot, and interact with it through the Chainlit UI.  
- Ask for the weather using a city name (e.g., "Find the weather in Islamabad").  



---
  
Enjoy using your AI-powered weather assistant! 🌍☀️  
```

