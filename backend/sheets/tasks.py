from celery import shared_task
import pypdfium2 as pdfium


@shared_task
def create_task_photo_of_pdf(pk, url, path):
    # find pdf document
    pdf = pdfium.PdfDocument(f"{path}")
    page = pdf.get_page(0)
    # name for photo
    output = f"{path[:-4]}.jpg"
    # render and save
    pil_image = page.render_topil()
    pil_image.save(output)
    # close page
    page.close()
    # add new phone in Model
    from sheets.models import Sheet

    Sheet.objects.filter(pk=pk).update(photo=f"{url[:-4]}.jpg")

    return True
