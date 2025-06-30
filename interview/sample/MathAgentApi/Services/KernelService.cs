using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Plugins.Core;
using Microsoft.SemanticKernel.Connectors.OpenAI;

namespace MathAgentApi.Services;

public class KernelService
{
    private readonly IKernel _kernel;

    public KernelService(IConfiguration config)
    {
        var builder = Kernel.Builder
            .WithOpenAIChatCompletionService(
                "gpt-3.5-turbo",
                "https://api.openai.com/v1/chat/completions",
                config["OpenAI:ApiKey"])
            .WithPlugin(new MathPlugin());

        _kernel = builder.Build();
    }

    public async Task<string> AddAsync(string prompt)
    {
        var result = await _kernel.RunAsync(prompt);
        return result.Result;
    }
}

public class MathPlugin
{
    [KernelFunction, Description("Adds two numbers together and provides the result")]
    public int AddNumbers(
        [Description("The first number to add")] int numberOne,
        [Description("The second number to add")] int numberTwo)
    {
        return numberOne + numberTwo;
    }
}
