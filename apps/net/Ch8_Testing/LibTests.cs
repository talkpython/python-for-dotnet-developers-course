using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace Ch8_Testing
{
    [TestClass]
    public class LibTests
    {
        //[TestMethod]
        //public void TestRunMeWrong()
        //{
        //    string style = "electric";

        //    Lib db = new Lib();
        //    Guitar[] guitars = db.AllGuitars(style);

        //    Assert.IsTrue(guitars.Length > 0);
        //    // Sweet little LINQ expression
        //    Assert.AreEqual(0, guitars.Count(g => g.Style != style));
        //}


        [TestMethod]
        public void TestElectricGuitars()
        {
            string style = "electric";

            Lib db = new Lib(TestData.GetMockDb(), TestData.GetMockLogger());
            Guitar[] guitars = db.AllGuitars(style);

            // Sweet little LINQ expression
            HashSet<string> set = guitars.Select(g => g.Style).ToHashSet();
            Assert.AreEqual(1, set.Count);
            CollectionAssert.Contains(set.ToArray(), style);
        }


        [TestMethod]
        public void TestAllGuitars()
        {
            Lib db = new Lib(TestData.GetMockDb(), TestData.GetMockLogger());
            Guitar[] guitars = db.AllGuitars("all");

            HashSet<string> set = guitars.Select(g => g.Style).ToHashSet();
            Assert.AreEqual(2, set.Count);
        }


        [TestMethod]
        [ExpectedException(typeof(ArgumentException))]
        public void TestInputValidation()
        {
            Lib db = new Lib(TestData.GetMockDb(), TestData.GetMockLogger());
            db.AllGuitars(null);
        }
    }
}
