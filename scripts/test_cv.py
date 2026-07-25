from app.ai.cv_service import CVService

service = CVService(
    "data/cv/Eric_Otieno_CV.pdf"
)

text = service.load_text()

print(text[:1000])