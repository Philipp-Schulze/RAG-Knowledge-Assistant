from views import history
from views import chat
from views import documents
from views import statistics

views = {
    chat.PAGE_KEY: {
        "label": chat.PAGE_NAME,
        "icon": chat.PAGE_ICON,
        "render": chat.render_chat,
    },
    history.PAGE_KEY: {
        "label": history.PAGE_NAME,
        "icon": history.PAGE_ICON,
        "render": history.render_history,
    },
    documents.PAGE_KEY: {
        "label": documents.PAGE_NAME,
        "icon": documents.PAGE_ICON,
        "render": documents.render_documents,
    },
    statistics.PAGE_KEY: {
        "label": statistics.PAGE_NAME,
        "icon": statistics.PAGE_ICON,
        "render": statistics.render_statistics,
    }
}