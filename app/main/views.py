 return render_template('index.html',title=title, general=cat_general, business = cat_business, entertainment = cat_entertainment, sports = cat_sports, tech = cat_tech, science = cat_science, health = cat_health)	    return render_template('index.html',title=title, general=cat_general, business = cat_business, entertainment = cat_entertainment, sports = cat_sports, tech = cat_tech, science = cat_science, health = cat_health)


 @main.route('/articles/<source_id>')	@main.route('/articles/<source_id>&<int:per_page>')
def articles(source_id):	def articles(source_id,per_page):
    '''	    '''
    Function that returns articles based on their sources	    Function that returns articles based on their sources
    '''	    '''
    # print(source_id)	    # print(source_id)
    per_page = 40	    # per_page = 40
    news_source = get_articles(source_id,per_page)	    news_source = get_articles(source_id,per_page)
    title = f'{source_id} | All Articles'	    title = f'{source_id} | All Articles'
    return render_template('articles.html', title = title, name = source_id, news = news_source)	    return render_template('articles.html', title = title, name = source_id, news = news_source)


 @main.route('/topheadlines')	@main.route('/topheadlines&<int:per_page>')
def headlines():	def headlines(per_page):
    '''	    '''
    Function that returns top headlines articles	    Function that returns top headlines articles
    '''	    '''
    per_page = 40	    # per_page = 40
    topheadlines_news = topheadlines(per_page)	    topheadlines_news = topheadlines(per_page)
    title = 'Top Headlines'	    title = 'Top Headlines'
    return render_template('topheadlines.html',title=title, name='Top Headlines' ,news=topheadlines_news)	    return render_template('topheadlines.html',title=title, name='Top Headlines' ,news=topheadlines_news)


 @main.route('/everything')	@main.route('/everything&<int:per_page>')
def all_news():	def all_news(per_page):
    '''	    '''
    Function that returns top headlines articles	    Function that returns top headlines articles
    '''	    '''
    per_page = 40	    # per_page = 40
    everything_news = everything(per_page)	    everything_news = everything(per_page)
    title = 'All News'	    title = 'All News'
