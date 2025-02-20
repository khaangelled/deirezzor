from flask import Flask, render_template, request

app = Flask(__name__)

def generate_post(title, program, episode, topic, category, youtube_link):
    youtube_title = f"{program} | الحلقة {episode} | {title}"
    
    youtube_description = f"""
    🎙️ استمع الآن إلى إذاعة دير الزور مباشرة! 🎙️
    🔴 تابعوا البث المباشر لإذاعتنا على موقعنا الرسمي:
    🌐 deirezzorfm.com
    
    📌 انضموا إلينا على فيسبوك لمتابعة آخر الأخبار والتحديثات:
    👍 صفحة الفيسبوك الرسمية
    https://www.facebook.com/profile.php?id=61569832435717
    
    ✨ لا تنسوا دعمنا بـ:
    ✅ الإعجاب بالفيديو ❤️
    ✅ الاشتراك في القناة 🔔
    ✅ ترك تعليق لتحفيزنا ✍️
    
    شكراً لكم على المتابعة!
    """
    
    facebook_teaser = f"🚀 لا تفوتوا الحلقة الجديدة من {program}! 🔥\n\n🎬 عنوان الحلقة: {title}\n🔍 الموضوع: {topic}\n\nلمتابعة البث المباشر لإذاعة دير الزور، يمكنكم زيارة:\n🌐 deirezzorfm.com"
    
    facebook_watch = f"🎥 شاهد الحلقة الجديدة الآن! 🎬\n\n📌 {youtube_title}\n🔍 {topic}\n\n🎥 رابط المشاهدة: {youtube_link if youtube_link else 'تابعونا عبر موقعنا'}\n\nلمتابعة البث المباشر لإذاعة دير الزور، يمكنكم زيارة:\n🌐 deirezzorfm.com"
    
    return youtube_title, youtube_description, facebook_teaser, facebook_watch

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        program = request.form['program']
        episode = request.form['episode']
        topic = request.form['topic']
        category = request.form['category']
        youtube_link = request.form.get('youtube_link', '')
        
        youtube_title, youtube_description, facebook_teaser, facebook_watch = generate_post(title, program, episode, topic, category, youtube_link)
        
        return render_template('index.html', youtube_title=youtube_title, youtube_description=youtube_description, 
                               facebook_teaser=facebook_teaser, facebook_watch=facebook_watch)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
