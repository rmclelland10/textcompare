import re

STOP_WORDS = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 
            'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some',
            'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's',
            'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the', 'themselves', 'until', 'below', 'are',
            'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more', 'himself',
            'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had',
            'she', 'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in',
            'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can',
            'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 
            'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 
            'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']

class TextCompare():
    def __init__(self, text1, text2):
        self.raw_text1 = text1
        self.raw_text2 = text2

    def decontracted(self, word):
        word = re.sub(r"won\'t", "will not", word)
        word = re.sub(r"can\'t", "can not", word)
        word = re.sub(r"n\'t", " not", word)
        word = re.sub(r"\'re", " are", word)
        word = re.sub(r"\'s", " is", word)
        word = re.sub(r"\'d", " would", word)
        word = re.sub(r"\'ll", " will", word)
        word = re.sub(r"\'t", " not", word)
        word = re.sub(r"\'ve", " have", word)
        word = re.sub(r"\'m", " am", word)
        return word

    def clean_text(self):
        # convert all words to lowercase
        self.text1 = self.raw_text1.lower()
        self.text2 = self.raw_text2.lower()
        
        # If string contains common conjuntion, convert conjunction to full term
        self.text1 = ' '.join([self.decontracted(word) for word in self.text1.split()])
        self.text2 = ' '.join([self.decontracted(word) for word in self.text2.split()])
        
        # Extract words, words with dash between (including dash)
        self.text1_words = re.findall(r"[a-z0-9\-]+[\-]?[a-z0-9%]+|[a-z0-9]|\([+-]\)", self.text1)
        self.text2_words = re.findall(r"[a-z0-9\-]+[\-]?[a-z0-9%]+|[a-z0-9]|\([+-]\)", self.text2)
        
        # Remove stop words
        self.text1 = ' '.join([word for word in self.text1_words if word not in STOP_WORDS])
        self.text2 = ' '.join([word for word in self.text2_words if word not in STOP_WORDS])

        # Update word vectors
        self.text1_words = self.text1.split()
        self.text2_words = self.text2.split()

    def compare_word_vectors(self):
        self.intersection = set(self.text1_words).intersection(set(self.text2_words))
        self.jaccard_sim = len(self.intersection) / (len(set(self.text1_words)) + len(set(self.text2_words)) - len(self.intersection))

    def compare(self):
        self.clean_text()
        try:
            self.compare_word_vectors()
            return {"text1": self.raw_text1, "text2": self.raw_text2, "score": self.jaccard_sim}
        except:
            return "Error occured when comparing text similarity."


if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser(description='Text Compare Exercise')
    p.add_argument('text1', type=str, help='text #1')
    p.add_argument('text2', type=str, help='text #2')
    args = p.parse_args()
    
    '''
    text1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. \
            If you have any participating brands on your receipt, you'll get points based on the cost of the products. \
            You don't need to clip any coupons or scan individual barcodes. \
            Just scan each grocery receipt after you shop and we'll find the savings for you."

    text2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. \
            If you have any eligible brands on your receipt, you will get points based on the total cost of the products. \
            You do not need to cut out any coupons or scan individual UPCs. \
            Just scan your receipt after you check out and we will find the savings for you."

    text3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. \
            These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. \
            No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. \
            We just think it is easier that way."
    '''

    tc = TextCompare(text1=args.text1, text2=args.text2)
    print(tc.compare())




