import { useState, useEffect } from "react";
import DiscList from "./DiscList";
import "./App.css";
import DiscForm from "./DiscForm";

function App() {
  const [discs, setDiscs] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentDisc, setCurrentDisc] = useState({})

  useEffect(() => {
    fetchDiscs()
  }, []);

  const fetchDiscs = async () => {
    const response = await fetch("http://127.0.0.1:5000/discs");
    const data = await response.json();
    setDiscs(data.discs);
  };

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentDisc({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (disc) => {
    if (isModalOpen) return
    setCurrentDisc(disc)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModal()
    fetchDiscs()
  }

  return (
    <>
      <DiscList discs={discs} updateDisc={openEditModal} updateCallback={onUpdate} />
      <button onClick={openCreateModal}>Create New Disc</button>
      {isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <DiscForm existingDisc={currentDisc} updateCallback={onUpdate} />
        </div>
      </div>
      }
    </>
  );
}

export default App;