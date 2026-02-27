using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Caching.Memory;
using assignment13.Services;

namespace assignment13.Controllers
{
    [Authorize]
    [ApiController]
    [Route("api/[controller]")]
    public class ProductController : ControllerBase
    {
        private readonly IMemoryCache _cache;
        private readonly ProductService _productService;
        private readonly ILogger<ProductController> _logger;

        public ProductController(IMemoryCache cache,
                                 ProductService productService,
                                 ILogger<ProductController> logger)
        {
            _cache = cache;
            _productService = productService;
            _logger = logger;
        }

        [HttpGet]
        public IActionResult GetProducts()
        {
            _logger.LogInformation("GetProducts API called");

            if (!_cache.TryGetValue("productList", out List<string>? products))
            {
                _logger.LogInformation("Cache miss. Fetching from service...");

                products = _productService.GetProducts();

                _cache.Set("productList", products,
                    new MemoryCacheEntryOptions
                    {
                        AbsoluteExpirationRelativeToNow = TimeSpan.FromMinutes(5)
                    });

                _logger.LogInformation("Products stored in cache");
            }
            else
            {
                _logger.LogInformation("Cache hit. Returning cached data");
            }

            return Ok(products);
        }
    }
}