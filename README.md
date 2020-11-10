# coding_challenge
Score similarity between two strings or texts.

## SET-UP
* git clone https://github.com/rmclelland10/textcompare.git
* cd to textcompare
* docker image build -t textcompare .
* docker run -p 5000:5000 textcompare

## EXAMPLE POST REQUESTS
TEXT1 compared to TEXT2
* curl -d '{"text1" : "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'\\''ll get points based on the cost of the products. You don'\\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\\''ll find the savings for you.", "text2" : "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."}' -H 'Content-Type: application/json' http://0.0.0.0:5000/compare

TEXT1 compared to TEXT3
 * curl -d '{"text1" : "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'\\''ll get points based on the cost of the products. You don'\\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\''ll find the savings for you.", "text2" : "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'\\''ll give you the points whether or not you knew about the offer. We just think it is easier that way."}' -H 'Content-Type: application/json' http://0.0.0.0:5000/compare

TEXT2 compared to TEXT3
* curl -d '{"text1" : "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you.", "text2" : "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'\\''ll give you the points whether or not you knew about the offer. We just think it is easier that way."}' -H 'Content-Type: application/json' http://0.0.0.0:5000/compare






