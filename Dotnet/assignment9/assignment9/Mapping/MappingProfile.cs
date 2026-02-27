using AutoMapper;
using assignment9.Models;
using assignment9.DTOs;

namespace assignment9.Mapping
{
    public class MappingProfile : Profile
    {
        public MappingProfile()
        {
            CreateMap<Student, StudentDto>().ReverseMap();
        }
    }
}
