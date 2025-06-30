# 🧠 Math Agent API using Semantic Kernel

This project is a C# ASP.NET Core API that uses Microsoft Semantic Kernel to let GPT choose and call C# functions.

## Features
- Accepts prompts like "Add 4 and 6"
- Uses GPT + Semantic Kernel function calling
- Calls typed C# functions reliably

## Usage

1. Add your OpenAI API key to appsettings.json
2. Run:
   dotnet restore
   dotnet run

3. Call:
POST http://localhost:5000/MathAgent/add
Body: { "prompt": "Add 10 and 25" }

Response: { "result": "The result is 35" }