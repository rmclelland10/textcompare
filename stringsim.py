import pandas as pd

class StringSim:

    def lowercase(self, text):
        # Convert all letters in string to lowercase
        return text.lower()

    def punct_convert(self, string, df):
        # If string contains common conjuntion, convert conjunction to full term
        conjunct_list = df.values
        for i in range(len(df)):
            string = string.replace(conjunct_list[i, 0].lower(), conjunct_list[i, 1].lower())
        return string
    
    def remove_stop_words(self, str_set):
        # Search for common stop words, remove them if found
        stopwords = dict({'Stops': ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 
            'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some',
            'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's',
            'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are',
            'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself',
            'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had',
            'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in',
            'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can',
            'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 
            'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 
            'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']})

        temp = set([])
        for i in str_set:
            if not i in [x for v in stopwords.values() for x in v]:
                temp.add(i)
        return temp

    def run(self, str1, str2):
        conjunctions_df = pd.read_excel("conjunctions.xlsx")

        # Convert to lowercase, remove conjunctions
        str1 = self.punct_convert(self.lowercase(str1), conjunctions_df)
        str2 = self.punct_convert(self.lowercase(str2), conjunctions_df)    

        # split string up in to set of words, remove stop words from each set
        a = set(str1.split())
        a = self.remove_stop_words(a)
        b = set(str2.split())
        b = self.remove_stop_words(b)

        # find intersection of two sets, calculate score based upon Jaccard Similarity
        c = a.intersection(b)
        return pd.DataFrame({'Score':[float(len(c)) / (len(a) + len(b) - len(c))]})

if __name__ == '__main__':
    str1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
    str2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
    str3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."
    s = StringSim()
    sim12 = s.run(str1, str2)['Score'][0] * 100
    sim13 = s.run(str1, str3)['Score'][0] * 100
    sim23 = s.run(str2, str3)['Score'][0] * 100
    print('Sample1 is %2.2f%% similar to Sample2' % (sim12))
    print('Sample1 is %2.2f%% similar to Sample3' % (sim13))
    print('Sample2 is %2.2f%% similar to Sample3' % (sim23))
