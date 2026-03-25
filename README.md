# MetaHarmonizer Curator Dashboard Prototype

This repository contains a simplified prototype of the **MetaHarmonizer Dashboard**
developed as part of the proposal for

GSoC 2026 – Automated Clinical Metadata Harmonization Dashboard

The goal of this prototype is to demonstrate the proposed curator workflow
and UI improvements for metadata harmonization in cBioPortal studies.

This is NOT the full MetaHarmonizer system.
It is a lightweight demo showing the dashboard interface and user interaction.

---

## Purpose

The current MetaHarmonizer pipeline provides automated schema and ontology mapping,
but the curator workflow requires a production-ready dashboard with better usability,
review tools, and integration with the cBioPortal data loading pipeline.

This prototype demonstrates the proposed UI design including:

- Upload metadata
- Mapping review interface
- Confidence score visualization
- Ontology mapping view
- Quality dashboard
- Export functionality

The final implementation will use React + FastAPI,
but this demo is built with Streamlit for rapid prototyping.

---

## Features in Prototype

- Upload CSV metadata file
- Automatic mock mapping generation
- Editable mapping review table
- Confidence score and stage display
- Filter low-confidence mappings
- Ontology mapping view (demo)
- Quality dashboard with metrics
- Export harmonized file

These features correspond to the required curator workflow:

Upload → Review → Ontology → Quality → Export

---

## Prototype Tech Stack

Prototype:
- Streamlit
- Pandas
- Python

Planned Final Implementation:
- React (frontend)
- FastAPI (backend)
- SQLite / PostgreSQL
- MetaHarmonizer ML engine
- REST API integration
- cBioPortal data loader integration

---

## How to Run

Clone the repository:

git clone https://github.com/yourusername/meta-harmonizer-dashboard-prototype

cd meta-harmonizer-dashboard-prototype



Install dependencies:
pip install -r requirements.txt
Run the app:
streamlit run app.py



The dashboard will open in your browser.

---

## Screenshots

Screenshots of the prototype UI are included in the `screenshots/` folder.

- Upload page
- Mapping review
- Ontology mapping
- Quality dashboard
- Export page

---

## Relation to MetaHarmonizer

This prototype is based on the existing MetaHarmonizer project:

https://github.com/shbrief/MetaHarmonizer

The current system provides the harmonization engine,
while this prototype focuses on improving the curator dashboard workflow.

---

## Proposed Improvements Over Current Dashboard

- Better mapping review interface
- Filtering and sorting support
- Batch actions
- Improved confidence visualization
- Validation before export
- Mapping history tracking (planned)
- Integration with cBioPortal loader (planned)

These improvements are described in the GSoC proposal document.

---

## License

Prototype created for educational and proposal purposes.
