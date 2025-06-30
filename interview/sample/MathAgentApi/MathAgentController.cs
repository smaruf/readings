using Microsoft.AspNetCore.Mvc;
using System.Threading.Tasks;
using MathAgentApi.Services;

namespace MathAgentApi.Controllers;

[ApiController]
[Route("[controller]")]
public class MathAgentController : ControllerBase
{
    private readonly KernelService _kernelService;

    public MathAgentController(KernelService kernelService)
    {
        _kernelService = kernelService;
    }

    [HttpPost("add")]
    public async Task<IActionResult> Add([FromBody] MathRequest req)
    {
        var result = await _kernelService.AddAsync(req.Prompt);
        return Ok(new { result });
    }
}

public record MathRequest(string Prompt);