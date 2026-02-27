namespace assignement4.Services
{
    public class MessageService : IMessageService
    {
        public string GetMessage()
        {
            return "This message is coming from Custom Service!";
        }
    }
}
