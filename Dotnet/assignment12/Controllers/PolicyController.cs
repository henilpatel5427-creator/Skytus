using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace assignment12.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class PolicyController : ControllerBase
    {
        [HttpGet]
        [Authorize(Policy = "UserOnly")]
        public IActionResult GetUserData()
        {
            return Ok("User Policy Access");
        }
    }
}