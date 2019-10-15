namespace Ch7_Db.Data
{
    public class Guitar
    {
        public int Id { get; set; }

        public string Name { get; set; }
        public float Price { get; set; }
        public string Img { get; set; }
        public string Style { get; set; }

        public Guitar()
        {
        }

        public Guitar(string name, float price, string img, string style)
        {
            Name = name;
            Price = price;
            Img = img;
            Style = style;
        }
    }
}
