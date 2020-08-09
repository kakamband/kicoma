from django.forms import ValidationError


# convert article amount or price between units, units are defined in .models.UNIT
def convertUnits(number, unitIn, unitOut):
    if unitIn == unitOut:
        return number
    if unitIn == 'kg' and unitOut == 'g':
        return number*1000
    if unitIn == 'g' and unitOut == 'kg':
        return number/1000
    if unitIn == 'l' and unitOut == 'ml':
        return number*100
    if unitIn == 'ml' and unitOut == 'l':
        return number/100
    print('ERROR: chyba konverze', number, unitIn, unitOut)
    raise ValidationError("Nedokáži provést {} konverzi {} na {}".format(number, unitIn, unitOut))


# returns total Article price, Article amount is converted using Article unit
def totalStockReceiptArticlePrice(stock_receipt_articles):
    total_price = 0
    for stock_receipt_article in stock_receipt_articles:
        convertedAmount = convertUnits(stock_receipt_article.amount,
                                       stock_receipt_article.unit, stock_receipt_article.article.unit)
        stock_receipt_article_price = convertedAmount * stock_receipt_article.price_with_vat
        print("totalStockReceiptArticlePrice: stock_receipt_article, stock_receipt_article_price, convertedAmount, stock_receipt_article.price_with_vat\n",
              stock_receipt_article, stock_receipt_article_price, convertedAmount, stock_receipt_article.price_with_vat)
        total_price += stock_receipt_article_price
    return total_price

# returns total RecipeArticle price, RecipeArticle amount is converted using Article unit
def totalRecipeArticlePrice(recipe_articles, norm_amount):
    total_price = 0
    for recipe_article in recipe_articles:
        convertedAmount = convertUnits(recipe_article.amount, recipe_article.unit, recipe_article.article.unit)
        recipe_article_price = convertedAmount * recipe_article.article.average_price * norm_amount
        total_price += recipe_article_price
    return total_price
