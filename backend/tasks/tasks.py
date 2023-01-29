from celery import shared_task
# import pypdfium2 as pdfium

# from sheets.models import Sheet


@shared_task
def create_task_photo_of_pdf(pk, path, url):
    # pdf = pdfium.PdfDocument(f"{path}")
    # page = pdf.get_page(0)
    # pil_image = page.render_topil()
    # output = f"{path[:-4]}.jpg"
    # pil_image.save(output)
    # page.close()
    print("Done")
    # Sheet.objects.filter(pk=pk).update(photo=f"{url[:-4]}.jpg")
    return True
