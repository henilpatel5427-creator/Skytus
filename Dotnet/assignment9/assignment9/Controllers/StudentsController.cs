using Microsoft.AspNetCore.Mvc;
using assignment9.Models;
using assignment9.DTOs;
using AutoMapper;

namespace assignment9.Controllers
{
    [ApiController]
    [ApiVersion("1.0")]
    [Route("api/v{version:apiVersion}/[controller]")]
    public class StudentsController : ControllerBase
    {
        private static List<Student> students = new()
        {
            new Student { Id = 1, Name = "Henil", Department = "CE", Marks = 85 }
        };

        private readonly IMapper _mapper;

        public StudentsController(IMapper mapper)
        {
            _mapper = mapper;
        }

        // GET ALL
        [HttpGet]
        public IActionResult GetAll()
        {
            return Ok(_mapper.Map<List<StudentDto>>(students));
        }

        // GET BY ID
        [HttpGet("{id}")]
        public IActionResult GetById(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null)
                return NotFound();

            return Ok(_mapper.Map<StudentDto>(student));
        }

        // POST
        [HttpPost]
        public IActionResult Create(StudentDto dto)
        {
            var student = _mapper.Map<Student>(dto);
            student.Id = students.Max(s => s.Id) + 1;

            students.Add(student);

            return CreatedAtAction(nameof(GetById),
                new { id = student.Id, version = "1.0" },
                _mapper.Map<StudentDto>(student));
        }

        // PUT
        [HttpPut("{id}")]
        public IActionResult Update(int id, StudentDto dto)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null)
                return NotFound();

            _mapper.Map(dto, student);
            return NoContent();
        }

        // DELETE
        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var student = students.FirstOrDefault(s => s.Id == id);
            if (student == null)
                return NotFound();

            students.Remove(student);
            return NoContent();
        }
    }
}
