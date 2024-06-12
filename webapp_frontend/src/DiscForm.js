import { useState } from "react";

const DiscForm = ({ existingDisc = {}, updateCallback }) => {
    const [disc_brand, setDiscBrand] = useState(existingDisc.disc_brand || "");
    const [disc_name, setDiscName] = useState(existingDisc.lastName || "");
    const [flight_speed, setFlightSpeed] = useState(existingDisc.email || "");
    const [flight_glide, setFlightGlide] = useState(existingDisc.email || "");
    const [flight_turn, setFlightTurn] = useState(existingDisc.email || "");
    const [flight_fade, setFlightFade] = useState(existingDisc.email || "");
    const [disc_plastic, setDiscPlastic] = useState(existingDisc.email || "");
    const [disc_weight, setDiscWeight] = useState(existingDisc.email || "");
    const [disc_notes, setDiscNotes] = useState(existingDisc.email || "");

    const updating = Object.entries(existingDisc).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            disc_brand,
            disc_name,
            flight_speed,
            flight_glide,
            flight_turn,
            flight_fade,
            disc_plastic,
            disc_weight,
            disc_notes
        }
        const url = "http://127.0.0.1:5000/" + (updating ? `update_disc/${existingDisc.id}` : "create_disc")
        const options = {
            method: updating ? "PATCH" : "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="discBrand">Disc Brand:</label>
                <input
                    type="text"
                    id="discBrand"
                    value={disc_brand}
                    onChange={(e) => setDiscBrand(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discName">Disc Name:</label>
                <input
                    type="text"
                    id="discName"
                    value={disc_name}
                    onChange={(e) => setDiscName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discFlightSpeed">Speed:</label>
                <input
                    type="number"
                    id="discFlightSpeed"
                    value={flight_speed}
                    onChange={(e) => setFlightSpeed(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discFlightGlide">Glide:</label>
                <input
                    type="number"
                    id="discFlightGlide"
                    value={flight_glide}
                    onChange={(e) => setFlightGlide(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discFlightTurn">Turn:</label>
                <input
                    type="number"
                    id="discFlightTurn"
                    value={flight_turn}
                    onChange={(e) => setFlightTurn(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discFlightFade">Fade:</label>
                <input
                    type="number"
                    id="discFlightFade"
                    value={flight_fade}
                    onChange={(e) => setFlightFade(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discPlastic">Plastic:</label>
                <input
                    type="text"
                    id="discPlastic"
                    value={disc_plastic}
                    onChange={(e) => setDiscPlastic(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discWeight">Weight (g):</label>
                <input
                    type="number"
                    id="discWeight"
                    value={disc_weight}
                    onChange={(e) => setDiscWeight(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="discNotes">Notes:</label>
                <input
                    type="text"
                    id="discNotes"
                    value={disc_notes}
                    onChange={(e) => setDiscNotes(e.target.value)}
                />
            </div>
            <button type="submit">{updating ? "Update" : "Create"}</button>
        </form>
    );
};

export default DiscForm