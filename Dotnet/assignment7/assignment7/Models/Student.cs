using System.ComponentModel.DataAnnotations;

namespace assignment7.Models
{
    public class Student
    {
        public int Id { get; set; }

        [Required]
        public string Name { get; set; }

        public string Department { get; set; }

        public int Marks { get; set; }
    }
}
