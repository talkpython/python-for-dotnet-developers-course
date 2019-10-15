using Ch6_Web.Data;
using Ch6_Web.Services;

namespace Ch6_Web.Models
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
