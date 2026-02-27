using Microsoft.AspNetCore.Mvc;
using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;

namespace assignment13.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class AuthController : ControllerBase
    {
        private readonly IConfiguration _configuration;
        private readonly ILogger<AuthController> _logger;

        public AuthController(IConfiguration configuration,
                              ILogger<AuthController> logger)
        {
            _configuration = configuration;
            _logger = logger;
        }

        // Simple Login (Demo Purpose)
        [HttpPost("login")]
        public IActionResult Login()
        {
            _logger.LogInformation("Login endpoint called");

            // Dummy user (for demo)
            var claims = new List<Claim>
            {
                new Claim(ClaimTypes.Name, "Henil"),
                new Claim(JwtRegisteredClaimNames.Jti, Guid.NewGuid().ToString())
            };

            var key = new SymmetricSecurityKey(
                Encoding.UTF8.GetBytes(_configuration["Jwt:Key"]!)
            );

            var token = new JwtSecurityToken(
                issuer: _configuration["Jwt:Issuer"],
                audience: _configuration["Jwt:Audience"],
                expires: DateTime.Now.AddMinutes(
                    Convert.ToDouble(_configuration["Jwt:DurationInMinutes"])
                ),
                claims: claims,
                signingCredentials: new SigningCredentials(
                    key,
                    SecurityAlgorithms.HmacSha256
                )
            );

            var tokenString = new JwtSecurityTokenHandler().WriteToken(token);

            _logger.LogInformation("JWT Token generated successfully");

            return Ok(new
            {
                token = tokenString,
                expiration = token.ValidTo
            });
        }
    }
}