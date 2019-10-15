using Ch7_Db.Data;
using Ch7_Db.Services;

namespace Ch7_Db.Models
{
    public class GuitarsViewModel
    {
        public string Style { get; }
        public Guitar[] Guitars { get; }

        public GuitarsViewModel(string style)
        {
            Style = style;
            Guitars = CatalogService.AllGuitars(style);
        }
    }
}
