from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_post(title, program, guest, topic, category, youtube_link):
    templates = {
        "خبر عاجل": f"🚨 عاجل: {title} - تفاصيل جديدة حول {topic} 📢",
        "خبر محلي": f"📍 {title} - تطورات محلية هامة في {topic} 🏡",
        "حلقات برامج": f"🎥 شاهد الآن: {program} | {title} مع {guest} 🔍 {topic}",
    }
    
    post_title = templates.get(category, f"📢 {title} - جديد على إذاعتنا")
    description = f"في هذه الحلقة/الخبر، نتناول موضوع {topic}. تابعونا عبر البث المباشر!"
    facebook_post = f"{post_title}\n\n{description}\n\n🎥 شاهد الآن: {youtube_link if youtube_link else 'تابعونا عبر موقعنا'}"
    
    return post_title, description, facebook_post

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        program = request.form.get('program', '')
        guest = request.form.get('guest', '')
        topic = request.form['topic']
        category = request.form['category']
        youtube_link = request.form.get('youtube_link', '')
        
        post_title, description, facebook_post = generate_post(title, program, guest, topic, category, youtube_link)
        
        return render_template('index.html', post_title=post_title, description=description, facebook_post=facebook_post)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
