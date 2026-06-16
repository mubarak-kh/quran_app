import streamlit as st 
import json,sys,os,re 
import base64
st.set_page_config(page_title="القرآن الكريم",page_icon="quran.png",layout="wide")
st.markdown("""
    <style>
        h1, h2, h3, .stTitle {
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

col1,col2,col3 = st.columns([1,2,1])
with col2:
    st.title('القرآن كريم ')
def get_path(filename):
    if getattr(sys, 'frozen', False):
        
        base_path = os.path.dirname(sys.executable)
    else:
        
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, filename)
with open(get_path("quran.json"), "r", encoding="utf-8") as f:
    quran = json.load(f)



with col2:
    
        
    with st.expander('عرض السور '):
        with st.container(height=400): 

            for surah in quran:
                with st.expander(f"سورة {surah['name']}",):
                    if surah['name']!="التوبة" :
                        st.write("**بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ**")
                    with st.container(height=400) :  
                        for i,verses in enumerate(surah['verses']):
                            col_a,col_b,col_c= st.columns([1,6,1])
                            with col_b:

                                st.markdown(f"""
        <div style='display: inline-block; direction: rtl; text-align: right; width: 100%;'>
            <span style='font-size: 18px;'>{verses['text']}</span>
            <span style='font-size: 16px; color: #2e86c1; font-weight: bold; margin-right: 5px;'>⟪{i+1}⟫</span>
        </div>
    """, unsafe_allow_html=True)
st.divider()
#***************دعاء ختم القرآن*************
col_tas1,col_tas2,col_tas3=st.columns([1,2,1])
with open(get_path("dooa_khatm.json"),"r",encoding="utf-8") as f:
    dooa_khatm=json.load(f)

with col_tas2:
    with st.expander("📖 دعاء ختم القرآن "):
        with st.container(height=400):
            for dooa in dooa_khatm['دعاء ختم القرآن']:
                st.write(f"{dooa}")
        
#**********************الأذكار*************    

st.divider()
colc,cold,cole=st.columns([1,2,1])

with cold:
    st.title('الأذكار ')  
with open(get_path("adhkar.json"),"r",encoding="utf-8") as f:
    adhkar_data=json.load(f)
col1,col2,col3=st.columns([1,2,1])

with col2:
    with st.expander("أذكار الصباح"):
        with st.container(height=400):
            for zikr in adhkar_data['الصباح']:
                st.write(f".{zikr}")
                st.divider()

    with st.expander("أذكار المساء"):
        with st.container(height=400):

            for zikr in adhkar_data['المساء']:
                st.write(f".{zikr}")
                st.divider()


    with st.expander("أذكار النوم"):
        with st.container(height=400):
            for zikr in adhkar_data['النوم']:
                st.write(f".{zikr}")
                st.divider()
            

#*************أدعية المنزل***********           
st.divider()
with open(get_path("dooa_doors.json"),"r",encoding="utf-8") as f:
    dooa_doors=json.load(f)
colc,cold,cole=st.columns([1,2,1])

with cold:
    st.title('أدعية المنزل ') 
col4,col5=st.columns([1,1])
with col4:
    with st.expander("أدعية الدخول"):
        with st.container(height=200):
            for zikr in dooa_doors['دخول المنزل']:
                st.write(f"{zikr}")
                st.divider()
with col5:
    with st.expander("أدعية الخروج"):
        with st.container(height=200):
            for zikr in dooa_doors['الخروج من المنزل']:
                st.write(f"{zikr}")
                st.divider()

#***********المسبحة الألكترونية********
st.divider()

    
colc,cold,cole=st.columns([1,2,1])
with cold:
    st.title("المسبحة الألكترونية ")
st.components.v1.html("""
    <div style='text-align: center;'>
        <h1 id='counter' style='font-size: 48px;color:red;'>0</h1>
        <button onclick='increase()' style='padding: 10px 20px; font-size: 20px; margin: 5px;'>➕ سبح</button>
        <button onclick='resetCounter()' style='padding: 10px 20px; font-size: 20px; margin: 5px;'>🔄 إعادة ضبط</button>
        <p style='font-size: 18px;'>المجموع الكلي: <span id='total'>0</span></p>
    </div>
    <script>
        let count = 0;
        let total = 0;
        function increase() {
            count++;
            total++;
            document.getElementById('counter').innerHTML = count;
            document.getElementById('total').innerHTML = total;
        }
        function resetCounter() {
            count = 0;
            document.getElementById('counter').innerHTML = count;
        }
    </script>
""", height=200)    

with st.expander("أذكار التسبيح 📖"):
    st.write("* سبحان الله *")
    st.write("* الحمد لله *")
    st.write("* لا إله إلا الله *")
    st.write("* الله أكبر * ")
    st.write("* لا حول ولا قوة إلا بالله *")
#*************عني***********
with st.sidebar:
    # CSS لجعل الصورة دائرية
    st.markdown("""
        <style>
            .sidebar-img {
                border-radius: 50% !important;
                width: 150px !important;
                height: 150px !important;
                object-fit: cover !important;
                border: 3px solid #2e86c1;
                display: block;
                margin: 20px auto;
            }
            .sidebar-text {
                text-align: center;
                font-family: 'Amiri', serif;
            }
        </style>
    """, unsafe_allow_html=True)
    
    
    st.markdown('<img src="data:image/jpeg;base64,{}" class="sidebar-img">'.format(
        get_base64_image("my.jpg")
    ), unsafe_allow_html=True)
    
    st.markdown("---")
    
    
    st.markdown("""
        <h3 style='text-align: center; color: #ff0000;'>مبارك خالد</h3>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    
    st.markdown("""
        <div style='text-align: center; background-color: #000000; padding: 15px; border-radius: 10px;'>
            <h4>🤲 صدقة جارية</h4>
            <p style='font-size: 16px;'>
                <b>اللهم اجعل هذا العمل صدقة جارية</b><br>
                <b>لي، ولوالديّ، ولجميع المسلمين</b><br>
                <i>اللهم اغفر لهم وارحمهم وتجاوز عنهم</i>
            </p>
            <p style='font-size: 14px; color: #555;'>
                📖 <i>"وَمَا أَرْسَلْنَاكَ إِلَّا رَحْمَةً لِّلْعَالَمِينَ"</i><br>
                (الأنبياء: 107)
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.caption("© 2026 مبارك خالد")

#**********************التذييل (Footer)*************
st.divider()

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("""
        <div style='text-align: center; direction: rtl;'>
            <p style='font-size: 14px; color: #555;'>
                📖 <b>تم تطوير هذا التطبيق بنية خدمة كتاب الله تعالى</b>
            </p>
            <p style='font-size: 13px; color: #777;'>
                🤲 <b>صدقة جارية</b> لي ولوالديّ ولجميع المسلمين
            </p>
            <p style='font-size: 12px; color: #999;'>
                © 2026 جميع الحقوق محفوظة | تصميم وتطوير: <b>مبارك خالد</b>
            </p>
            <p style='font-size: 11px; color: #aaa;'>
                📱 للتواصل: <i>تم تطويره بنية خالصة لوجه الله تعالى</i>
            </p>
        </div>
    """, unsafe_allow_html=True)














