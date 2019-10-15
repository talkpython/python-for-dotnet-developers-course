namespace Ch8_Testing
{
    public class Guitar
    {
        public string Name { get; }
        public float Price { get; }
        public string Img { get; }
        public string Style { get; }

        public Guitar(string name, float price, string img, string style)
        {
            Name = name;
            Price = price;
            Img = img;
            Style = style;
        }
    }
}
