namespace assignment9.DTOs
{
    public class StudentDto
    {
        public int Id { get; set; }
        public required string Name { get; set; }
        public required string Department { get; set; }
        public int Marks { get; set; }
    }
}
